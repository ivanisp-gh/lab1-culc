import pytest

from decimal import Decimal

from toolkit.converter import convert, type_line
from toolkit.errors import NegativeDistanceError, BelowAbsoluteZeroError


def test_length():
    assert convert("1mm") == "1.0mm - 0.1cm - 0.001m - 0.000001km"
    assert convert("1cm") == "10.0mm - 1.0cm - 0.01m - 0.00001km"
    assert convert("1m") == "1000.0mm - 100.0cm - 1.0m - 0.001km"
    assert convert("1km") == "1000000.0mm - 100000.0cm - 1000.0m - 1.0km"


def test_length_comma():
    assert convert("2,5m") == "2500.0mm - 250.0cm - 2.5m - 0.0025km"


def test_length_space():
    assert convert("  2 KM  ") == "2000000.0mm - 200000.0cm - 2000.0m - 2.0km"
    assert convert(" 15 CM ") == "150.0mm - 15.0cm - 0.15m - 0.00015km"


def test_temp_celsius():
    assert convert("0C") == "0.0C - 32.0F - 273.15K"
    assert convert("100C") == "100.0C - 212.0F - 373.15K"
    assert convert("-273.15C") == "-273.15C - -459.67F - 0.0K"


def test_temp_farengheit():
    assert convert("32F") == "0.0C - 32.0F - 273.15K"
    assert convert("212F") == "100.0C - 212.0F - 373.15K"


def test_temp_kelvin():
    assert convert("273.15K") == "0.0C - 32.0F - 273.15K"
    assert convert("373.15K") == "100.0C - 212.0F - 373.15K"


def test_temp_space():
    assert convert("0 C") == "0.0C - 32.0F - 273.15K"
    assert convert("32  F") == "0.0C - 32.0F - 273.15K"
    assert convert("273.15 K") == "0.0C - 32.0F - 273.15K"


def test_weight():
    assert convert("1g") == "1.0g - 0.001kg"
    assert convert("1000g") == "1000.0g - 1.0kg"
    assert convert("1kg") == "1000.0g - 1.0kg"
    assert convert("2.5kg") == "2500.0g - 2.5kg"


def test_weight_space_comma():
    assert convert("2,5 kg") == "2500.0g - 2.5kg"
    assert convert(" 500 G ") == "500.0g - 0.5kg"


def test_type_line():
    assert type_line("12cm") == ["length", Decimal("12"), "cm"]
    assert type_line("25,5 kg") == ["weight", Decimal("25.5"), "kg"]
    assert type_line("32F") == ["temp", Decimal("32"), "f"]
    assert type_line(" 0 C ") == ["temp", Decimal("0"), "c"]


def test_negative_length():
    with pytest.raises(NegativeDistanceError):
        convert("-1mm")

    with pytest.raises(NegativeDistanceError):
        convert("-2.5m")

    with pytest.raises(NegativeDistanceError):
        convert("-1km")


def test_temp_below_zero():
    with pytest.raises(BelowAbsoluteZeroError):
        convert("-274C")

    with pytest.raises(BelowAbsoluteZeroError):
        convert("-500F")

    with pytest.raises(BelowAbsoluteZeroError):
        convert("-1K")


def test_wrong_input():
    with pytest.raises(ValueError):
        convert("hello")

    with pytest.raises(ValueError):
        convert("10")

    with pytest.raises(ValueError):
        convert("5l")

    with pytest.raises(ValueError):
        convert("12 meters")

    with pytest.raises(ValueError):
        convert("kg")

    with pytest.raises(ValueError):
        convert("10CC")