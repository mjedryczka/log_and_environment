'''My Calculator Test'''

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import divide

def test_calculation_operations(a, b, operation, expected):
    """ Test calculation operations with various scenarios. """
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_divide_by_zero():
    """ Test division by zero to ensure it raises a ValueError. """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
