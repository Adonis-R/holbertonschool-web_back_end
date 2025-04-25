#!/usr/bin/env python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a caching system using MRU eviction algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.use_order = []

    def put(self, key, item):
        """ Add an item in the cache using MRU policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.use_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Supprimer le plus récemment utilisé
            mru_key = self.use_order.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.use_order.append(key)

    def get(self, key):
        """ Get an item by key and mark it as most recently used """
        if key is None or key not in self.cache_data:
            return None

        self.use_order.remove(key)
        self.use_order.append(key)
        return self.cache_data[key]
