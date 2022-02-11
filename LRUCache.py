"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

This solution is being implemented using OrderedDict.
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.od.keys():
            self.od.move_to_end(key)
            return self.od[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.od.keys():
            self.od.move_to_end(key)
        if len(self.od) == self.capacity:
            self.od.popitem(last=False)
        self.od[key] = value

if __name__ == "__main__":
    LRU = LRUCache(5)
    LRU.put('a', 5)
    LRU.put('b', 6)
    LRU.put('c', 7)
    LRU.put('d', 8)
    LRU.put('e', 9)
    LRU.put('f', 10)
    print(LRU.get('i'))
    print(LRU.get('f'))
    LRU.put('a', 12)
    print(LRU.get('a'))
