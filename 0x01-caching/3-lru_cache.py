#!/usr/bin/python3
"""
BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Defines LRUCache class that inherits from `BaseCaching`
    """
    def __init__(self):
        """Initialize"""
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """Add an item in cache"""
        if key and item:
            if key in self.cache_data.keys():
                self.stack.remove(key)
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                discard_key = self.stack[0]
                del (self.cache_data[discard_key])
                self.stack.remove(discard_key)
                print("DISCARD: {}".format(discard_key))
            self.stack.append(key)

    def get(self, key):
        """Get an item from cache"""
        if key and key in self.cache_data.keys():
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache_data[key]
        else:
            return None
