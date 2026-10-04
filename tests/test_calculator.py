import pytest
from toolkit.calculator import calculation
from toolkit.errors import DivisionByZeroError


def test_base_calculations():
    assert calculation("2+2*2") == "6.0"
    assert calculation("(2+2)*2") == "8.0"
    assert calculation("2+2*-2") == "-2.0"
    assert calculation("(2+2*2)//7") == "0.0"
    assert calculation("(2+2*2)%7") == "6.0"
    assert calculation("(2+2*2)/2*2//2%2") == "1.0"
    assert calculation("2*3") == "6.0"
    assert calculation("10/2") == "5.0"
    assert calculation("2*3+4") == "10.0"
    assert calculation("10+6/2") == "13.0"


def test_added_functions():
    assert calculation("7//2") == "3.0"
    assert calculation("7%2") == "1.0"
    assert calculation("10//3") == "3.0"
    assert calculation("10%3") == "1.0"


def test_minus_signs():
    assert calculation("-2+3") == "1.0"
    assert calculation("-2*3") == "-6.0"
    assert calculation("2*-3") == "-6.0"
    assert calculation("-2*-3") == "6.0"


def test_floats():
    assert calculation("2.5+2.5") == "5.0"
    assert calculation("5.0/2") == "2.5"
    assert calculation("2.5*4") == "10.0"


def test_parentheses():
    assert calculation("(2+3)*4") == "20.0"
    assert calculation("2*(3+4)") == "14.0"
    assert calculation("(2+3)*(4+1)") == "25.0"
    assert calculation("((2+3)*4)+1") == "21.0"
    assert calculation("(2+2*2)") == "6.0"
    assert calculation("((2+2)*2)") == "8.0"


def test_divisionbyzero():
    with pytest.raises(DivisionByZeroError):
        calculation("5/0")
    with pytest.raises(DivisionByZeroError):
        calculation("5//0")
    with pytest.raises(DivisionByZeroError):
        calculation("5%0")




def test_space():
    assert calculation("2 + 2") == "4.0"
    assert calculation(" 2 * 3 ") == "6.0"
    assert calculation("10 / 2 + 3") == "8.0"