import pytest
from calculator import add, subtract, multiply, divide

def test_add():
     assert add(1 ,2) == 3
     assert add(5 ,5) == 10
     assert add(-1 ,1) == 0
     assert add(-1 ,-1) == -2
     assert add(0 ,0) == 0

def test_subtract():
     assert subtract(2 ,1) == 1
     assert subtract(5 ,5) == 0
     assert subtract(-6 ,-12) == 6
     assert subtract(10 ,-12) == 22
     assert subtract(0 ,0) == 0

def test_multiply():
     assert multiply(2 ,1) == 2
     assert multiply(5 ,5) == 25
     assert multiply(-6 ,-12) == 72
     assert multiply(10 ,-12) == -120
     assert multiply(0 ,0) == 0


def test_divide():
     assert divide(2 ,1) == 2
     assert divide(5 ,5) == 1
     assert divide(-6 ,-6) == 1
     assert divide(10 ,-10) == -1
     assert divide(1 ,1) == 1
