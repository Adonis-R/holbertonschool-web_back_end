#!/usr/bin/env python3
'''Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing the
following key-value pairs:'''
import csv
import math
from typing import Dict, Any, List

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''return the correct page of the dataset'''
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        '''Return a dictionary with pagination information'''
        # Obtain the requested page using the get_page method
        data = self.get_page(page, page_size)

        # Calculate the total number of items in the dataset
        total_items = len(self.dataset())

        # Calculate the total number of pages
        total_pages = math.ceil(total_items / page_size)

        # Determine the next page and the previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Build the response dictionary
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
