#!/usr/bin/env python3
"""Simple pagination"""

import csv
import math
from typing import List, Tuple, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get a page with pagination"""
        cp = self.get_page(page, page_size)
        tp = math.ceil(len(self.__dataset) / page_size)
        np = page + 1
        pp = page - 1

        return {
            'page_size': len(cp),
            'page': page,
            'data': cp,
            'next_page': np if tp >= np else None,
            'prev_page': pp if pp > 0 else None,
            'total_pages': tp
        }

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page with pagination"""
        assert isinstance(page, int) and isinstance(page_size, int), "a"
        assert page > 0 and page_size > 0, "page and page_size must be > 0"
        start, end = index_range(page, page_size)
        idx = []
        self.dataset()
        for i in range(start, end):
            try:
                idx.append(self.__dataset[i])
            except IndexError as e:
                return []
        return idx
