# https://practice.geeksforgeeks.org/problems/8c8f95810b05b4cab665f2997d36991bd58308a2/1

class Solution:
    def Reduced_String(self, k, s):
        # Your code goes here
        # return the reduced string
        if k==1:
            return ''
        st=[]
        for ch in s:
            if len(st) and st[-1][0]==ch:
                st[-1][1]+=1
                if st[-1][1]==k:
                    st.pop()
            else:
                st.append([ch,1])
        str1=""
        for ele in st:
            str1 += ele[0]*ele[1]
        return str1
s1=Solution()
k = 2
s = "geegsforgeeeks"
# k=5
# s='obiwjjruufcejzuvviojktiyhiaxulnqolpfcvkaiywhrrxezrybgyetmpulspmjzmcgbuhfhdvuccuydtolfpakoyscfylwjass'
print(s1.Reduced_String(k,s))

# obiwjrufcejzuviojktiyhiaxulnqolpfcvkaiywhrxezrybgyetmpulspmjzmcgbuhfhdvucuydtolfpakoyscfylwjas
# obiwjjruufcejzuvviojktiyhiaxulnqolpfcvkaiywhrrxezrybgyetmpulspmjzmcgbuhfhdvuccuydtolfpakoyscfylwjass

