from .cordic_funcs import is_even, is_odd, sgn


def basic_pow(base: float, exponent: int) -> float:
    """Integer `pow` function."""
    if exponent != int(exponent):
        msg = "`exponent` must be an integer."
        raise ValueError(msg)
    if base == exponent == 0:
        msg = "`0**0` is undefined."
        raise ValueError(msg)

    return pow(base, exponent)  # Let python handle it efficiently.


def factorial(n: int) -> int:
    """Compute n! (factorial of n)."""
    if n != int(n) or n < 0:
        msg = "`n` must be a non-negative integer."
        raise ValueError(msg)

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


__all__ = ["basic_pow", "factorial", "is_even", "is_odd", "sgn"]
