from typing import Union
import math

NumType = Union[int, float]


def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
    try:
        numerator = round(12 * a + 25 * b, 2)
        denominator = round(1 + a ** (2**b), 2)
        result = round(numerator / denominator, 2)
    except (OverflowError, ZeroDivisionError):
        result = 0

    return result
