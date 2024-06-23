from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import divide
from app.commands import Command
import pytest


class DivideCommand(Command):
    def execute(self, numberA: str, numberB: str):
        calculation = Calculation(Decimal(numberA), Decimal(numberB), divide)
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            print(calculation.perform())