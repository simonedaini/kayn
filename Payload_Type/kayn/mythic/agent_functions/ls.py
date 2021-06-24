from mythic_payloadtype_container.MythicCommandBase import *
import json
from mythic_payloadtype_container.MythicRPC import *
import sys

class LsArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {
            "path": CommandParameter(
                name="path",
                type=ParameterType.String,
                default_value=".",
                description="Path of file or folder on the current system to list",
            )
        }

    async def parse_arguments(self):
        if len(self.command_line) > 0:
            if self.command_line[0] == '{':
                temp_json = json.loads(self.command_line)
                if 'host' in temp_json:
                    # this means we have tasking from the file browser rather than the popup UI
                    # the apfell agent doesn't currently have the ability to do _remote_ listings, so we ignore it
                    if temp_json['file'] != "":
                        self.add_arg("path", temp_json['path'].replace("\\", "/") + "/" + temp_json['file'])
                    else: 
                        self.add_arg("path", temp_json['path'].replace("\\", "/"))
                else:
                    self.add_arg("path", temp_json['path'].replace("\\", "/"))
                self.add_arg("file_browser", "true")
            else:
                self.add_arg("path", self.command_line)
                self.add_arg("file_browser", "true")


class LsCommand(CommandBase):
    cmd = "ls"
    needs_admin = False
    help_cmd = "ls /path/to/file"
    description = "Get attributes about a file and display it to the user via API calls. No need for quotes and relative paths are fine"
    version = 1
    supported_ui_features = ["file_browser:list"]
    author = "@its_a_feature_"
    attackmapping = ["T1106", "T1083"]
    argument_class = LsArguments
    browser_script = BrowserScript(script_name="ls", author="@its_a_feature_")

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        resp = await MythicRPC().execute("create_artifact", task_id=task.id,
            artifact="fileManager.attributesOfItemAtPathError, fileManager.contentsOfDirectoryAtPathError",
            artifact_type="API Called",
        )
        if task.args.has_arg("file_browser") and task.args.get_arg("file_browser"):
            host = task.callback.host
            task.display_params = host + ":" + task.args.get_arg("path")
        else:
            task.display_params = task.args.get_arg("path")
        return task

    async def process_response(self, response: AgentResponse):
        pass
