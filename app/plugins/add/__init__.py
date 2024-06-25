from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add
from app.commands import Command
import logging


class AddCommand(Command):
    def execute(self, numberA: str, numberB: str):
        calculation = Calculation(Decimal(numberA), Decimal(numberB), add)
        result = calculation.perform()
        logging.info(result)
        print(result)