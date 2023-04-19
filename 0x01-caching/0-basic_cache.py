#!/usr/bin/python3
"""
BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
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

    def get(self, key):
        """Get an item from cache"""
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
