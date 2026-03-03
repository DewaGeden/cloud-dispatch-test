"""乘法和除法模块的测试用例"""

import pytest
from calculator.mul_div import divide, multiply


def test_multiply_positive():
    """测试正整数乘法"""
    assert multiply(3, 4) == 12


def test_multiply_negative():
    """测试负数乘法"""
    assert multiply(-3, 4) == -12
    assert multiply(-3, -4) == 12


def test_multiply_zero():
    """测试与零相乘"""
    assert multiply(0, 100) == 0
    assert multiply(100, 0) == 0


def test_multiply_float():
    """测试浮点数乘法"""
    assert multiply(1.5, 2.0) == pytest.approx(3.0)


def test_divide_positive():
    """测试正整数除法"""
    assert divide(10, 2) == 5.0


def test_divide_negative():
    """测试负数除法"""
    assert divide(-10, 2) == -5.0
    assert divide(-10, -2) == 5.0


def test_divide_float():
    """测试浮点数除法"""
    assert divide(7.5, 2.5) == pytest.approx(3.0)


def test_divide_by_zero():
    """测试除零异常"""
    with pytest.raises(ValueError, match="除数不能为零"):
        divide(10, 0)
