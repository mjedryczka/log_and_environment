from abc import ABC, abstractmethod
from decimal import Decimal

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        try:
            userInput = command_name.lower().strip().split(" ")
            # print(userInput, command_name)
            if len(userInput) == 3:
                self.commands[userInput[0]].execute(userInput[1], userInput[2])
            elif len(userInput) == 1:
                self.commands[userInput[0]].execute()
            else:
                print("Usage: <operation> <numberA> <numberB>")

        except KeyError:
            print(f"No such command: {command_name}")