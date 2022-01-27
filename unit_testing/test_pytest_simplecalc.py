# Pytest
from unit_testing.simplecalc import SimpleCalc
import pytest


def test_calc_add():
    calc = SimpleCalc()
    assert calc.add(2, 6) == 8


def test_calc_subtract():
    calc = SimpleCalc()
    assert calc.subtract(6, 2) == 4


def test_calc_multiply():
    calc = SimpleCalc()
    assert pytest.approx(calc.multiply(0.4, -80.9)) == -32.36


def test_calc_divide():
    calc = SimpleCalc()
    assert calc.divide(10, 2) == 5


def test_calc_divide_by_zero_raises_error():
    calc = SimpleCalc()
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)

