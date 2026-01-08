"""Tests for precomputed values used in CORDIC algorithm."""

import math

import pytest

from CORDIC.precompute import PRECOMPUTED_ATAN

atans = [math.atan(2**-i) for i in range(len(PRECOMPUTED_ATAN))]


@pytest.mark.parametrize(("ours", "theirs"), zip(PRECOMPUTED_ATAN, atans, strict=True))
def test_precomputed_atan(ours: float, theirs: float) -> None:
    """Check that we match the `math` module."""
    assert ours == pytest.approx(theirs)
