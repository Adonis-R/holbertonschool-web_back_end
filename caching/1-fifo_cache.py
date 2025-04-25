#!/usr/bin/env python3
"""
FIFOCache module that implements a caching system using FIFO
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that removes the oldest item first
    when the limit is reached. It inherits from BaseCaching.
    """

    def __init__(self):
        """
        Initialize the FIFOCache instance and call the parent constructor.
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache.

        If the cache exceeds MAX_ITEMS, discard the oldest item (FIFO).
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    oldest_key = self.queue.pop(0)
                    del self.cache_data[oldest_key]
                    print(f"DISCARD: {oldest_key}")
            else:
                # If key already exists, remove it to re-add at
                # the end of the queue
                self.queue.remove(key)

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """
        Retrieve an item by key.

        Returns:
            The value in self.cache_data associated with the key, or None.
        """
        return self.cache_data.get(key)
