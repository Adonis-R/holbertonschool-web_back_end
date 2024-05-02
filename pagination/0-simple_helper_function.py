#!/usr/bin/env python3

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start = (page - 1) * page_size
    end = (page_size * page)
    return (start, end)
