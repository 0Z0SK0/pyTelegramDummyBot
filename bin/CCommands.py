import CConfig
import CExceptions
import CFunctions
import CDatabase

import json
import asyncio

class CCommands():
    def __init__(self):
        self.commands = {}

        CONFIG_PATH = CConfig.CConfig().getConfigDirectory() + "\\commands.json"

        with open(CONFIG_PATH) as config:
            data = json.load(config)

            for i in data['commands']:
                for key in i:
                    self.commands[key] = i[key]

    async def interpret(self, command, chat_id, message_id):
        if command in self.commands:
            try: 
                return await eval(f"CFunctions.CFunctions().{self.commands[command]}({chat_id}, {message_id})")
            except NameError: raise CExceptions._FunctionNotFound("Executable function for command not found.")
        else:
            raise CExceptions._CommandNotFound("Input command not found.")