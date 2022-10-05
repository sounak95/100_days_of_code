

class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        n= len(arr)
        nge= [-1]* n
        st=[]
        st.append(0)
        for i in range(1,n):
            ele= arr[i]
            while st and ele>arr[st[-1]]:
                index = st.pop()
                nge[index] =ele
            st.append(i)
        if len(st)!=0:
            for idx in st:
                nge[idx] = -1

        return nge

s=Solution()
print(s.nextLargerElement([1,3,2,4], 4))