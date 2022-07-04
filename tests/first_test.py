import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calulate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calulate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5
