#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that uses LIFO (Last In First Out) strategy.
    """

    def __init__(self):
        """ Initialize the cache and the stack """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item to the cache.

        If the cache exceeds MAX_ITEMS, discard the last item added.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.stack.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.stack.pop()
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

            self.cache_data[key] = item
            self.stack.append(key)

    def get(self, key):
        """
        Get an item by key from the cache.

        Returns the value, or None if not found.
        """
        return self.cache_data.get(key)
