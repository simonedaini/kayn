from mythic_payloadtype_container.MythicCommandBase import *
import json


class TunnelArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class TunnelCommand(CommandBase):
    cmd = "tunnel"
    needs_admin = False
    help_cmd = "tunnel"
    description = "returns SSH credentials and opens a tunnel using SSHuttle, executing the command over the tunnel"
    version = 1
    supported_ui_features = [""]
    author = "@Kayn93"
    argument_class = TunnelArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
