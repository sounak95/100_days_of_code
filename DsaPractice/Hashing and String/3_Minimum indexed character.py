
# https://practice.geeksforgeeks.org/problems/minimum-indexed-character-1587115620/1


class Solution:

    # Function to find the minimum indexed character.
    def minIndexChar(self, Str, pat):
        map={}
        for i, ch in enumerate(Str):
            if ch not in map:
                map[ch] = i

        index=float('inf')
        for ch in pat:
            if ch in Str:
                index= min(index, map[ch])
        if index ==float('inf'):
            index=-1
        return index


# code here
s=Solution()
print(s.minIndexChar("adcffaet", "onkl"))
