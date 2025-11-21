"""Mathematical functions using CORDIC algorithm."""


def is_even(x: int) -> bool:
    """Check if a number is even."""
    if x != int(x):
        msg = "Argument must be an integer."
        raise ValueError(msg)
    return (x & 1) == 0


def is_odd(x: int) -> bool:
    """Check if a number is odd."""
    return not is_even(x)


def sgn(x: float) -> int:
    """Return the sign of the number."""
    return 1 if x >= 0 else -1


__all__ = ["is_even", "is_odd", "sgn"]
