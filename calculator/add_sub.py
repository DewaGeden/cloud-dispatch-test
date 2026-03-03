"""加法和减法模块"""


def add(a: int | float, b: int | float) -> int | float:
    """计算两个数的和。

    参数:
        a: 第一个加数，支持 int 和 float
        b: 第二个加数，支持 int 和 float

    返回:
        a 与 b 的和
    """
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """计算两个数的差。

    参数:
        a: 被减数，支持 int 和 float
        b: 减数，支持 int 和 float

    返回:
        a 减去 b 的差
    """
    return a - b
