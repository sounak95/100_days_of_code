
# https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st1=[]

        for ch in s:
            if ch!='#':
                st1.append(ch)
            else:
                if len(st1)!=0:
                    st1.pop()
        str1= "".join(st1)

        st2=[]

        for ch in t:
            if ch!='#':
                st2.append(ch)
            else:
                if len(st2) != 0:
                    st2.pop()
        str2= "".join(st2)

        return str1==str2

s=Solution()
print(s.backspaceCompare("ab#c", "ad#c"))
print(s.backspaceCompare("a#c", "b"))