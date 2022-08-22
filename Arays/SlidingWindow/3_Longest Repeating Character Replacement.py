
# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l=0
        count={}
        res=0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1

            while(r-l+1-max(count.values()) >k):
                count[s[l]]-=1
                l+=1

            res= max(res, r-l+1)
        return res

s=Solution()
str = "AABABBA"
k=1
print(s.characterReplacement(str,k))
