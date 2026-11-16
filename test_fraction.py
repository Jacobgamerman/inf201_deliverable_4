import pytest
from Deliverable_4_Task_2 import Fraction


def test_initialization_and_simplification():
    f1 = Fraction(2, 4)
    assert f1.numerator == 1
    assert f1.denominator == 2

    f2 = Fraction(-6, 9)
    assert f2.numerator == -2
    assert f2.denominator == 3


def test_invalid_initialization():
    with pytest.raises(ValueError):
        Fraction(1, 0)
    with pytest.raises(ValueError):
        Fraction(1, -5)
    with pytest.raises(TypeError):
        Fraction(1.5, 2)
    with pytest.raises(TypeError):
        Fraction(1, "2")


def test_string_representations():
    assert str(Fraction(3, 4)) == "3/4"
    assert str(Fraction(4, 2)) == "2"
    assert repr(Fraction(1, 2)) == "Fraction(1, 2)"


def test_comparisons():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)
    f3 = Fraction(3, 4)

    assert f1 == f2
    assert f1 != f3
    assert f1 < f3
    assert f1 <= f2
    assert f1 <= f3
    assert f3 > f1
    assert f3 >= f1
    assert f2 >= f1


def test_arithmetic_operations():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)

    assert f1 + f2 == Fraction(5, 6)
    assert f1 - f2 == Fraction(1, 6)
    assert f1 * f2 == Fraction(1, 6)
    assert f1 / f2 == Fraction(3, 2)

    with pytest.raises(ZeroDivisionError):
        _ = f1 / Fraction(0, 1)