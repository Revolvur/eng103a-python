# Pytest
from unit_testing.simplecalc import SimpleCalc
import pytest


@pytest.fixture
def calc():
    return SimpleCalc()


def test_calc_add(calc):
    calc = SimpleCalc()
    assert calc.add(2, 6) == 8


def test_calc_subtract(calc):
    calc = SimpleCalc()
    assert calc.subtract(6, 2) == 4


def test_calc_multiply(calc):
    calc = SimpleCalc()
    assert pytest.approx(calc.multiply(0.4, -80.9)) == -32.36


def test_calc_divide(calc):
    calc = SimpleCalc()
    assert calc.divide(10, 2) == 5


def test_calc_divide_by_zero_raises_error(calc):
    calc = SimpleCalc()
    with pytest.raises(ZeroDivisionError):
        calc.divide(1, 0)
