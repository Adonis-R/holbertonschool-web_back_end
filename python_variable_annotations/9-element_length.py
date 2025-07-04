#!/usr/bin/env python3
"""Annotate the below functions parameters and return
values with the appropriate types"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples, each tuple containing an element"""
    return [(i, len(i)) for i in lst]
