"""Series expansions for pre-computed arctangents."""

from .higher_math import basic_pow, factorial, is_even


def arctan_taylor_term(*, n: int, z: float) -> float:
    """Nth term of the arctangent Taylor series for `z`."""
    if abs(z) > 1:
        msg = f"No taylor series for at z = {z}."
        raise ValueError(msg)
    sign = 1 if is_even(n) else -1
    numerator = basic_pow(z, 2 * n + 1)
    denominator = 2 * n + 1
    return sign * numerator / denominator


def arctan_from_taylor_series(z: float, *, prec: float = 1e-6) -> float:
    """Compute arctan(z) using its Taylor series expansion."""
    n = 0
    total = 0.0
    taylor_term = arctan_taylor_term(n=n, z=z)
    while abs(taylor_term) > prec / 100:
        total += taylor_term
        n += 1
        taylor_term = arctan_taylor_term(n=n, z=z)
    return total


def arctan_euler_accelerated_term(*, n: int, z: float) -> float:
    """Nth term of the Euler-accelerated arctangent series for `z`."""
    # \arctan(z) = \sum_{n=0}^\infty \frac{2^{2n} (n!)^2}{(2n + 1)!} \frac{z^{2n + 1}}{(1 + z^2)^{n + 1}}  # noqa: E501
    # https://en.wikipedia.org/w/index.php?title=Arctangent_series&oldid=1310174733#:~:text=Euler%27s%20formula%20above%20can%20be%20simplified%20and%20expressed%20as%5B6%5D
    numerator = (
        basic_pow(2, 2 * n) * basic_pow(factorial(n), 2) * basic_pow(z, 2 * n + 1)
    )
    denominator = factorial(2 * n + 1) * basic_pow(1 + basic_pow(z, 2), n + 1)
    return numerator / denominator


def arctan_euler_accelerated(z: float, *, prec: float = 1e-6) -> float:
    """Compute arctan(z) using Euler-accelerated series expansion."""
    n = 0
    total = 0.0
    series_term = arctan_euler_accelerated_term(n=0, z=z)
    while abs(series_term) > prec / 100:
        total += series_term
        n += 1
        series_term = arctan_euler_accelerated_term(n=n, z=z)
    return total
