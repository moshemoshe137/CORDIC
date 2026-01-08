"""Create a table of precomputed arctangents."""

from CORDIC import MAX_ITERS
from CORDIC.funcs.series import arctan_euler_accelerated

PRECOMPUTED_ATAN = [
    arctan_euler_accelerated(2**-i, prec=1e-32) for i in range(MAX_ITERS)
]

__all__ = ["PRECOMPUTED_ATAN"]
