#!/usr/bin/env python3
"""
Type-annotated function element_length that takes a list of strings lst as argument
and returns a list of integers representing the lengths of the strings.
"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
