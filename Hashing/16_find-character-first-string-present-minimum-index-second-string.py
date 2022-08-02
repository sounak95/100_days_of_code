# https://www.geeksforgeeks.org/find-character-first-string-present-minimum-index-second-string/


class Solution:

    # Function to find the minimum indexed character.
    def minIndexChar(self, Str, pat):
        map={}
        for i, ch in enumerate(Str):
            if ch not in map:
                map[ch] =i

        min_index = float('inf')
        for ch in pat:
            if ch in map:
                min_index = min(min_index, map[ch])

        if min_index == float('inf'):
            return -1
        return min_index

s=Solution()
print(s.minIndexChar("geeksforgeeks", "set"))
