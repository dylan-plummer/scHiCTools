"""
PyHiC
__author__ == 'Fan Feng'
=======

For conveniently dealing with single cell HiC data.

"""

from .ContactMaps import scHiCs
from .load_hic_file import *

__all__ = ["scHiCs",
    "get_chromosome_lengths",
    "file_line_generator",
    "load_HiC"
]