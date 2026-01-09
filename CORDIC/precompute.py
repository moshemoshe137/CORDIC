"""Create a table of precomputed arctangents."""

from CORDIC.funcs.series import arctan_euler_accelerated
from CORDIC.options import options

PRECOMPUTED_ATAN = [
    arctan_euler_accelerated(2**-i, prec=1e-32) for i in range(options["max_iters"])
]

__all__ = ["PRECOMPUTED_ATAN"]
