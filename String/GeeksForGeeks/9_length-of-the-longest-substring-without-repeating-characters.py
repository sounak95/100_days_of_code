# https://practice.geeksforgeeks.org/problems/longest-distinct-characters-in-string5848/1



class Solution:

    def longestSubstrDistinctChars(self, S):
        # code here
        left=0
        right=0
        n= len(S)
        m={}
        ans=""
        max_len=float('-inf')
        while(left<n and right<n):
            el = S[right]
            if el in m:
                left=max(left, m[el]+1)
            m[el]= right
            sunstr = S[left:right+1]

            if len(sunstr)> max_len:
                ans=sunstr
                max_len = max(len(sunstr), max_len)
            right+=1
        print((ans))
        return max_len

s=Solution()
print(s.longestSubstrDistinctChars("geeksforgeeks"))


