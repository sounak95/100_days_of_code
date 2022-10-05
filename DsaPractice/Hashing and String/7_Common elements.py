
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-hashing/problem/common-elements1132

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        A.sort()
        B.sort()
        C.sort()
        i=0
        j=0
        k=0
        l1=[]
        while(i<n1 and j<n2 and k<n3):
            if A[i]==B[j]==C[k]:
                if A[i] not in l1:
                    l1.append(A[i])
            if A[i]< B[j]:
                i+=1
            elif B[j]<C[k]:
                j+=1
            else:
                k+=1
        return l1

s=Solution()
s.commonElements()

