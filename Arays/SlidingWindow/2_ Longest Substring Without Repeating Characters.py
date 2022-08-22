

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        charSet = set()
        res=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res= max(res, len(charSet))

        return res


s=Solution()
str = "abcabcbb"
print(s.lengthOfLongestSubstring(str))

