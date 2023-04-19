#!/usr/bin/python3
"""
BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines BasicCache class that inherits from `BaseCaching`
    """
    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Add an item in cache"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                discard_key = next(iter(self.cache_data))
                del (self.cache_data[discard_key])
                print("DISCARD: ", discard_key)

    def get(self, key):
        """Get an item from cache"""
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
