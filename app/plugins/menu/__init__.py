import sys
from app.commands import Command
import logging


class MenuCommand(Command):
    def execute(self):
        logging.info("Printing Menu")
        print(f'Menu')
        print(f'Exit')
        print(f'Add')
        print(f'Subtract')
        print(f'Multiply')
        print(f'Divide')