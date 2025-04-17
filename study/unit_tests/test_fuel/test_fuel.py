# Then, in a file called test_fuel.py, implement two or more functions that collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_ so that you can execute your tests with:


import pytest
from alt_fuel import convert, gauge

def test_convert_valid_input():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("0/100") == 0
    assert convert("100/100") == 100

def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("hello/world")
    with pytest.raises(ValueError):
        convert("1/")
    with pytest.raises(ValueError):
        convert("/2")

def test_convert_zero_division():
    with pytest.raises(ValueError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge_valid_input():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == 50
    assert gauge(2) == 2
    assert gauge(98) == 98
