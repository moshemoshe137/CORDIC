"""Test functions in the higher_math module."""

import math

import pytest

from CORDIC.funcs.higher_math import basic_pow, factorial


class TestBasicPow:
    """Test the basic_pow function."""

    @pytest.mark.parametrize(
        ("n", "exponent", "expected"),
        [
            (2, 3, 8),
            (5, 0, 1),
            (1 / 3, 5, 1 / 243),
            (1.1, 16, 4.594972705722207),
        ],
    )
    def test_basic_pow(self, n: float, exponent: int, expected: float) -> None:
        """Test the basic_pow function."""
        # Regular, positive exponents
        assert (
            basic_pow(n, exponent)
            == n**exponent
            == pow(n, exponent)
            == math.pow(n, exponent)
            == pytest.approx(expected)
        )

        # Negative exponents
        assert (
            basic_pow(n, -exponent)
            == n**-exponent
            == pow(n, -exponent)
            == math.pow(n, -exponent)
            == pytest.approx(1 / expected)
        )

    @pytest.mark.parametrize("zero1", [0, 0.0])
    @pytest.mark.parametrize("zero2", [0, 0.0])
    def test_basic_pow_zero_zero(self, zero1: float, zero2: float) -> None:
        """Test that 0**0 raises ValueError."""
        with pytest.raises(ValueError, match=r"`0\*\*0` is undefined\."):
            basic_pow(zero1, zero2)  # type: ignore[arg-type]

    @pytest.mark.parametrize("base", [0, 1, -1, 2.5, -3.5])
    @pytest.mark.parametrize(
        "exponent", [2.5, -1.1, 0.01, 3.14, float("nan"), float("inf"), float("-inf")]
    )
    def test_basic_pow_non_integer_exponent(self, base: float, exponent: float) -> None:
        """Test that non-integer exponents raise ValueError."""
        matches = [
            r"`exponent` must be an integer\.",
            r"cannot convert float (NaN|infinity) to integer",
        ]
        with pytest.raises((ValueError, OverflowError), match="|".join(matches)):
            basic_pow(base, exponent)  # type: ignore[arg-type]


class TestFactorial:
    """Test the factorial function."""

    factorials = (
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (7, 5040),
        (10, 3628800),
        (15, 1307674368000),
        (
            100,
            93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000,
        ),
    )

    @pytest.mark.parametrize(("n", "expected"), factorials)
    def test_factorial(self, n: int, expected: int) -> None:
        """Test the factorial function."""
        assert factorial(n) == math.factorial(n) == expected

    @pytest.mark.parametrize("n", [-1, -5, -10])
    def test_factorial_negative(self, n: int) -> None:
        """Test that negative n raises ValueError."""
        with pytest.raises(ValueError, match=r"`n` must be a non-negative integer\."):
            factorial(n)

    @pytest.mark.parametrize(
        "n", [2.5, -1.1, float("nan"), float("inf"), float("-inf")]
    )
    def test_factorial_non_integer(self, n: float) -> None:
        """Test that non-integer n raises ValueError."""
        matches = [
            r"`n` must be a non-negative integer\.",
            "cannot convert float (NaN|infinity) to integer",
        ]
        with pytest.raises((ValueError, OverflowError), match="|".join(matches)):
            factorial(n)  # type: ignore[arg-type]
