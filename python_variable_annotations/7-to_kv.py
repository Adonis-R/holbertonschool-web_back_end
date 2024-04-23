#!/usr/bin/env python3
"""Type-annotated function to_kv that takes a string k and an
int OR float v as arguments and returns a tuple. The first element
of the tuple is the string k. The second element is the square of
the int/float v and
should be annotated as a float."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string k and the square of the int/float v.
    """
    sqr = float(v**2)
    t = (k, sqr)
    return t
