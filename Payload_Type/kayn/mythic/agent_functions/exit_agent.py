from mythic_payloadtype_container.MythicCommandBase import *
import json


class ExitArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class ExitCommand(CommandBase):
    cmd = "exit_agent"
    needs_admin = False
    help_cmd = "exit"
    description = "This exits the current prova instance by leveraging the exit() method."
    version = 1
    supported_ui_features = ["callback_table:exit"]
    author = ""
    argument_class = ExitArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
