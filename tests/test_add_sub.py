"""加法和减法模块的测试"""

import pytest
from calculator.add_sub import add, subtract


# 加法测试
def test_add_positive():
    """测试正数相加"""
    assert add(3, 5) == 8


def test_add_negative():
    """测试负数相加"""
    assert add(-4, -6) == -10


def test_add_zero():
    """测试与零相加"""
    assert add(7, 0) == 7
    assert add(0, 0) == 0


def test_add_float():
    """测试浮点数相加"""
    assert add(1.5, 2.5) == pytest.approx(4.0)


# 减法测试
def test_subtract_positive():
    """测试正数相减"""
    assert subtract(10, 4) == 6


def test_subtract_negative():
    """测试负数相减"""
    assert subtract(-3, -7) == 4


def test_subtract_zero():
    """测试减去零"""
    assert subtract(5, 0) == 5
    assert subtract(0, 0) == 0


def test_subtract_float():
    """测试浮点数相减"""
    assert subtract(3.5, 1.5) == pytest.approx(2.0)
