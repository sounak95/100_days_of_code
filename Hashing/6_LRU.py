# https://leetcode.com/problems/lru-cache/

from collections import deque
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c= capacity
        self.m = {}
        self.cache = deque()
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.m:
            self.cache.remove(key)
            self.cache.append(key)
            return self.m[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.m:
            if len(self.cache)==self.c:
                oldest= self.cache.popleft()
                del self.m[oldest]
        else:
            self.cache.remove(key)
        self.m[key]= value
        self.cache.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)