#!/usr/bin/env python3
""" LRUCache module
"""
from caching.base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines a caching system using LRU eviction algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.use_order = []

    def put(self, key, item):
        """ Add an item in the cache using LRU policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the value and usage
            self.use_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Evict the least recently used item
            lru_key = self.use_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        # Add item and update usage
        self.cache_data[key] = item
        self.use_order.append(key)

    def get(self, key):
        """ Get an item by key and mark it as recently used """
        if key is None or key not in self.cache_data:
            return None

        # Update usage
        self.use_order.remove(key)
        self.use_order.append(key)
        return self.cache_data[key]
