# https://www.geeksforgeeks.org/find-the-first-repeated-character-in-a-string/

class Solution:

    def firstRepChar(self, s):
        # code here
        hash=set()
        for ch in s:
            if ch in hash:
                return ch
            else:
                hash.add(ch)
        return ""