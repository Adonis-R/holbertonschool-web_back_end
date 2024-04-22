#!/usr/bin/env python3
"""
This module contains the sum_list function
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    t = 0
    for num in input_list:
        t += num
    return float(t)
