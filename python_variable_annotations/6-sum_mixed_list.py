#!/usr/bin/env python3
"""
This module contains the sum_mixed_list function
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums the elements of a list of mixed floats and integers.
    """
    t = 0
    for num in mxd_lst:
        t += num
    return float(t)
