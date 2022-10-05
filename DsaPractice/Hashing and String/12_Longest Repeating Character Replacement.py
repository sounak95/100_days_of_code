
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
        max_len=0
        for r in range(len(s)):
            ch=s[r]
            count[ch] = count.get(ch,0)+1

            while(r-l+1-max(count.values())>k):
                count[s[l]]-=1
                l+=1

            max_len = max(max_len, r-l+1)
        return max_len
s=Solution()
s1 = "ABAB"
k = 2
print(s.characterReplacement(s1,k))
