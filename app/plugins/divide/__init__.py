from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import divide
from app.commands import Command
import logging


class DivideCommand(Command):
    def execute(self, numberA: str, numberB: str):
        if numberB == "0":
            logging.info("Cannot divide by zero")
            print("Cannot divide by zero")
        else:
            calculation = Calculation(Decimal(numberA), Decimal(numberB), divide)
            result = calculation.perform()
            logging.info(result)
            print(result)