# https://leetcode.com/problems/valid-palindrome-ii/

class Solution(object):

    def validSubPalindrome(self,s, left, right):

        while(left<right):
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left=0
        right = len(s)-1

        while(left<right):
            if s[left]!=s[right]:
                return self.validSubPalindrome(s,left+1, right) or self.validSubPalindrome(s,left, right-1)
            left+=1
            right-=1
        return True

s= Solution()
print(s.validPalindrome("aba"))
print(s.validPalindrome("abc"))