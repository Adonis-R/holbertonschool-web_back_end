#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list which takes a
list mxd_lst of integers and floats and returns their sum as a float."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats."""
    return sum(mxd_lst)
