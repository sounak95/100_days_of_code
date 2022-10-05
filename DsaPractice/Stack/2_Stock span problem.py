

# https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1

class Solution:

    # Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a):
        n=len(a)
        st=[]
        st.append(0)
        s=[0]*n
        s[0] =1
        for i in range(1,n):
            ele=a[i]
            while st and ele>=a[st[-1]]:
                st.pop()
            if len(st)==0:
                s[i] = i+1
            else:
                s[i] = i-st[-1]

            st.append(i)

        return s

s=Solution()
print(s.calculateSpan([100,80,60,70,60,75,85]))


# code here