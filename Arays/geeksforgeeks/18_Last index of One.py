
# https://practice.geeksforgeeks.org/problems/last-index-of-15847/1

class Solution:
    def lastIndex(self, s):
        # code here
        for i in range(len(s)-1, -1, -1):
            if s[i]=='1':
                return i
        return -1
