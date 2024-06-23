import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print(f'Menu')
        print(f'Exit')
        print(f'Add')
        print(f'Subtract')
        print(f'Multiply')
        print(f'Divide')