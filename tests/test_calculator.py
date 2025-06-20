import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0) 