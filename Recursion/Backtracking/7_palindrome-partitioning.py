
# https://leetcode.com/problems/palindrome-partitioning/

class Solution(object):

    def isPalindrome(self, s, start, end):
        while(start<=end):
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True


    def func(self, index, s, path, res):
        if index==len(s):
            res.append(path.copy())
            return

        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i):
                path.append(s[index:i+1])
                self.func(i+1,s,path, res)
                path.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        self.func(0,s,[], res)
        return res
