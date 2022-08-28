
# https://leetcode.com/problems/valid-anagram/

# use hashing to store frequency of elements

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        count_s={}
        count_t={}

        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            count_s[s[i]]= count_s.get(s[i], 0) +1
            count_t[t[i]]= count_t.get(t[i], 0) +1

        for c in count_s:
            if count_s[c] != count_t.get(c,0):
                return False

        return True


s=Solution()
print(s.isAnagram("rat", "car"))