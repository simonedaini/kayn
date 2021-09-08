from mythic_payloadtype_container.MythicCommandBase import *
import json


class KeylogArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class KeylogCommand(CommandBase):
    cmd = "keylog"
    needs_admin = False
    help_cmd = "keylog"
    description = "Keylog users as root on Linux."
    version = 1
    supported_ui_features = []
    author = "@Kayn93"
    argument_class = KeylogArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
