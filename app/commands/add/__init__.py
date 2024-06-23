from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add
from app.commands import Command


class AddCommand(Command):
    def execute(self, numberA: str, numberB: str):
        calculation = Calculation(Decimal(numberA), Decimal(numberB), add)
        print(calculation.perform())