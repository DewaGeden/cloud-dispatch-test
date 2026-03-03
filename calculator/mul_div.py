"""乘法和除法模块"""


def multiply(a: float, b: float) -> float:
    """计算两个数的乘积。

    参数:
        a: 被乘数，支持 int 和 float
        b: 乘数，支持 int 和 float

    返回:
        a 与 b 的乘积
    """
    return a * b


def divide(a: float, b: float) -> float:
    """计算两个数的商。

    参数:
        a: 被除数，支持 int 和 float
        b: 除数，支持 int 和 float，不能为零

    返回:
        a 除以 b 的结果

    异常:
        ValueError: 当除数 b 为零时抛出
    """
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b
