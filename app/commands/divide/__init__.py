from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import divide
from app.commands import Command


class DivideCommand(Command):
    def execute(self, numberA: str, numberB: str):
        calculation = Calculation(Decimal(numberA), Decimal(numberB), divide)
        print(calculation.perform())