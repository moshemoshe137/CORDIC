"""Test functions in the CORDIC module."""

from collections.abc import Callable

import pytest

from CORDIC.funcs.cordic_funcs import is_even, is_odd, sgn

# even_odd_integers_param =


@pytest.mark.parametrize("func", [is_even, is_odd])
class TestIsEvenOdd:
    """Test the is_even and is_odd functions."""

    @pytest.mark.parametrize(
        ("input_int", "expected"),
        [
            (0, True),
            (2, True),
            (-4, True),
            (3, False),
            (-5, False),
            (1_000_000, True),
            (1_000_001, False),
        ],
    )
    def test_is_even_odd(
        self, *, input_int: int, expected: bool, func: Callable[[int], bool]
    ) -> None:
        """Test the is_even and is_odd functions."""
        if func.__name__ == "is_even":
            assert func(input_int) == expected
        elif func.__name__ == "is_odd":
            assert func(input_int) == (not expected)
        else:
            msg = f"Invalid function {func.__name__} provided to test."
            raise ValueError(msg)

    @pytest.mark.parametrize("float_input", [3.5, -2.1, "10", "-9.99"])
    def test_is_even_odd_float(
        self, float_input: float | str, func: Callable[[int], bool]
    ) -> None:
        """Test is_even with invalid input."""
        msgs = [
            r"Argument must be an integer\.",
            rf"invalid literal for int\(\) with base 10: '{float_input}'",
        ]
        with pytest.raises(ValueError, match="|".join(msgs)):
            func(float_input)  # type: ignore[arg-type]

    @pytest.mark.parametrize("float_input", [float("inf"), float("-inf"), float("nan")])
    def test_is_even_odd_inf_nan(
        self, float_input: float, func: Callable[[int], bool]
    ) -> None:
        """Test is_even with inf and nan."""
        with pytest.raises(
            (OverflowError, ValueError),
            match=r"cannot convert float (infinity|NaN) to integer",
        ):
            func(float_input)  # type: ignore[arg-type]


class TestSgn:
    """Test the sgn function."""

    @pytest.mark.parametrize(
        ("input_value", "expected"),
        [
            (10.5, 1),
            (0.0, 1),
            (-0.0, 1),
            (-3.2, -1),
            (float("inf"), 1),
            (float("-inf"), -1),
            (float("nan"), -1),  # By definition in our sgn function
        ],
    )
    def test_sgn(self, input_value: float, expected: int) -> None:
        """Test the sgn function."""
        assert sgn(input_value) == expected
