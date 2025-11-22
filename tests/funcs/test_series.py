"""Tests for series expansions."""

import math
from typing import ClassVar

import pytest

from CORDIC.funcs.series import (
    arctan_euler_accelerated,
    arctan_euler_accelerated_term,
    arctan_from_taylor_series,
    arctan_taylor_term,
)


class TestArctan:
    """Test the arctan series expansions."""

    arctangents: ClassVar[dict[float, float]] = {
        0: 0,
        1 / 3: math.atan(1 / 3),
        1 / 10: math.atan(1 / 10),
        999 / 1000: math.atan(999 / 1000),
        -1 / 6: math.atan(-1 / 6),
        0.9: math.atan(0.9),
        1 / math.pi: math.atan(1 / math.pi),
    }

    @pytest.mark.parametrize(
        ("z", "n", "expected"),
        [
            (0, 0, 0),
            (0, 1, 0),
            (0, 10, 0),
            (1 / 3, 0, 1 / 3),
            (1 / 3, 25, -pow(1 / 3, 51) / 51),
            (1 / 10, 100, -pow(1 / 10, 201) / 201),
            (999 / 1000, 50, pow(999 / 1000, 101) / 101),
            (-1 / 6, 0, -1 / 6),
            (-1 / 6, 10, -pow(-1 / 6, 21) / 21),
            (-1 / 6, 100, -pow(-1 / 6, 201) / 201),
            (0.9, 25, -pow(0.9, 51) / 51),
            (1 / math.pi, 10, pow(math.pi, -21) / 21),
        ],
    )
    def test_arctan_taylor_term(self, z: float, n: int, expected: float) -> None:
        """Test arctan_taylor_term function."""
        assert arctan_taylor_term(n=n, z=z) == pytest.approx(expected)

    @pytest.mark.parametrize(
        "z",
        [1.1, 2, -3, -1.5, float("inf"), float("-inf"), math.pi, -math.e],
        ids=lambda z: f"z={z:.2f}".rstrip("0").rstrip("."),  # For "rounding"
    )
    @pytest.mark.parametrize("n", [2**x for x in range(0, 12, 2)], ids="n={:,}".format)
    def test_arctan_taylor_term_invalid(self, z: float, n: int) -> None:
        """Test arctan_taylor_term with invalid input."""
        with pytest.raises(ValueError, match=f"No taylor series for at z = {z}"):
            arctan_taylor_term(n=n, z=z)

    @pytest.mark.parametrize(
        ("z", "expected"), arctangents.items(), ids=[f"z={z:.6f}" for z in arctangents]
    )
    @pytest.mark.parametrize("prec", [1e-6, 1e-8, 1e-10], ids="prec={}".format)
    def test_arctan_from_taylor_series(
        self, z: float, prec: float, expected: float
    ) -> None:
        """Test arctan_from_taylor_series function."""
        calculated = arctan_from_taylor_series(z, prec=prec)
        assert calculated == pytest.approx(expected, abs=prec)

    @pytest.mark.parametrize(
        ("z", "n", "expected"),
        [
            (0, 0, 0),
            (0, 1, 0),
            (0, 10, 0),
            (1 / 3, 0, 3 / 10),
            (-1 / 3, 0, -3 / 10),
            (1 / 3, 5, 4 / 3_609_375),
            (1 / 10, 1, 20 / 30_603),
            (1 / 10, 10, 2_621_440 / 10_821_637_105_466_104_336_435_885_869),
            (99 / 100, 0, 9_900 / 19_801),
            (99 / 100, 1, 64_686_600 / 392_079_601),
            (99 / 100, 50, 3.33376992839925454917181400409182696909208677525527697e-17),
        ],
    )
    def test_arctan_euler_accelerated_term(
        self, z: float, n: int, expected: float
    ) -> None:
        """Test arctan_euler_accelerated_term function."""
        assert arctan_euler_accelerated_term(n=n, z=z) == pytest.approx(expected)

    @pytest.mark.parametrize(
        ("z", "expected"), arctangents.items(), ids=[f"z={z:.6f}" for z in arctangents]
    )
    @pytest.mark.parametrize("prec", [1e-6, 1e-8, 1e-10], ids="prec={}".format)
    def test_arctan_euler_accelerated(
        self, z: float, prec: float, expected: float
    ) -> None:
        """Test arctan_euler_accelerated function."""
        calculated = arctan_euler_accelerated(z, prec=prec)
        assert calculated == pytest.approx(expected, abs=prec)
