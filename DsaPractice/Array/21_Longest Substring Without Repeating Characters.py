
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        chr_set=set()
        max_len = 0
        for r in range(len(s)):
            while(s[r] in chr_set):
                l+=1
                chr_set.remove(s[l])
            chr_set.add(s[r])
            max_len = max(max_len, len(chr_set))
        return max_len



