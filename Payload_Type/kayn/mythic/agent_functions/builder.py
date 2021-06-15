from PayloadBuilder import *
import asyncio
import os
from distutils.dir_util import copy_tree
import tempfile

# define your payload type class here, it must extend the PayloadType class though
class MyNewPayload(PayloadType):

    name = "prova"  # name that would show up in the UI
    file_extension = "py"  # default file extension to use when creating payloads
    author = "@Kayn93"  # author of the payload type
    supported_os = [SupportedOS.Linux]  # supported OS and architecture combos
    wrapper = False  # does this payload type act as a wrapper for another payloads inside of it?
    wrapped_payloads = []  # if so, which payload types. If you are writing a wrapper, you will need to modify this variable (adding in your wrapper's name) in the builder.py of each payload that you want to utilize your wrapper.
    note = "Prova agent python"
    supports_dynamic_loading = True  # setting this to True allows users to only select a subset of commands when generating a payload
    build_parameters = {}
    #  the names of the c2 profiles that your agent supports
    c2_profiles = ["HTTP"]
    # after your class has been instantiated by the mythic_service in this docker container and all required build parameters have values
    # then this function is called to actually build the payload
    async def build(self) -> BuildResponse:
        # this function gets called to create an instance of your payload
        resp = BuildResponse(status=BuildStatus.Error)

        try:
            command_code = ""
            for cmd in self.commands.get_commands():
                command_code += (
                    open(self.agent_code_path / "{}.py".format(cmd), "r").read() + "\n\n\n"
                )

            base_code = open(
                self.agent_code_path / "base_agent.py", "r"
            ).read()
            base_code = base_code.replace("UUID_HERE", self.uuid)
            base_code = base_code.replace("# FUNCTIONS", command_code)


            for c2 in self.c2info:
                profile = c2.get_c2profile()["name"]
                for key, val in c2.get_parameters_dict().items():
                    base_code = base_code.replace(key, val)

            resp.payload = base_code.encode()
            resp.status = BuildStatus.Success
            resp.message = "Successfully built!"

        except Exception as e:
                    resp.set_status(BuildStatus.Error)
                    resp.set_message("Error building payload: " + str(e))

        return resp
