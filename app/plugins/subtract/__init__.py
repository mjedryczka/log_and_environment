from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import subtract
from app.commands import Command
import logging

class SubtractCommand(Command):
    def execute(self, numberA: str, numberB: str):
        calculation = Calculation(Decimal(numberA), Decimal(numberB), subtract)
        result = calculation.perform()
        logging.info(result)
        print(result)