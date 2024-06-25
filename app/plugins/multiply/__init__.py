from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import multiply
from app.commands import Command
import logging

class MultiplyCommand(Command):
    def execute(self, numberA: str, numberB: str):
        calculation = Calculation(Decimal(numberA), Decimal(numberB), multiply)
        result = calculation.perform()
        logging.info(result)
        print(result)