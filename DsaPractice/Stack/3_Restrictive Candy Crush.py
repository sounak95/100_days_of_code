
# https://practice.geeksforgeeks.org/problems/8c8f95810b05b4cab665f2997d36991bd58308a2/1

class Solution:
    def Reduced_String(self, k, s):
        # Your code goes here
        # return the reduced string
        st=[]

        for ch in s:
            if st  and st[-1][0] == ch:
                st[-1][1]+=1
                if st[-1][1]==k:
                    st.pop()
            else:
                st.append([ch,1])
        str1=""
        for ch in st:
            str1+=ch[0] * ch[1]

        return str1

s=Solution()
print(s.Reduced_String(2,"geegsforgeeeks"))