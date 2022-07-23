
# https://leetcode.com/problems/backspace-string-compare/

class Solution(object):

    def backspaceCompare(self,s,t):
        p1=len(s)-1
        p2=len(t)-1

        while(p1>=0 or p2>=0):
            if (p1>=0 and s[p1]=='#') or (p2>=0 and t[p2]=='#'):
                if p1>=0 and s[p1]=='#'=='#':
                    back_space=2
                    while(back_space>0):
                        p1-=1
                        back_space-=1
                        if p1>=0 and s[p1]=='#':
                            back_space+=2
                if p2>=0 and t[p2]=='#':
                    back_space=2
                    while(back_space>0):
                        p2-=1
                        back_space-=1
                        if p2>=0 and t[p2]=='#':
                            back_space+=2
            else:
                if p1>=0 and p2<0 or p1<0 and p2>=0:
                    return False
                if s[p1]!=t[p2]:
                    # print(p1,p2)
                    # print(s[p1],t[p2])
                    return False
                else:
                    p1-=1
                    p2-=1

        return True
    def backspaceCompare_brute_force(self, s, t):
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
        print(str1,str2)
        return str1==str2

s=Solution()
# print(s.backspaceCompare("ab#c", "ad#c"))
# print(s.backspaceCompare("a#c", "b"))
# print(s.backspaceCompare("ab##", "c#d#"))
s1="aaa###a"
t="aaaa###a"

# s1="nzp#o#g"
# t="b#nzp#o#g"
s1="bxj##tw"
t="bxj###tw"

s1="a#c###"
t="ad#c"
print(s.backspaceCompare(s1,t))
# print(s.backspaceCompare_brute_force(s1,t))