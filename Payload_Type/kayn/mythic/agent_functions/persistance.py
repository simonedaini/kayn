from CommandBase import *
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
    is_exit = False
    is_file_browse = False
    is_process_list = False
    is_download_file = False
    is_remove_file = False
    is_upload_file = False
    author = "@Kayn93"
    argument_class = PersistanceArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass
