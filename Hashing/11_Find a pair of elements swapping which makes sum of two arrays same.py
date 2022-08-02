# https://www.geeksforgeeks.org/find-a-pair-swapping-which-makes-sum-of-two-arrays-same/

class Solution:

    def getSum(self,A):
        sum=0
        for ele in A:
            sum+=ele
        return sum

    def getTarget(self,A,B):

        sum_a = self.getSum(A)
        sum_b = self.getSum(B)

        if (sum_a-sum_b)%2!=0:
            return float('-inf')

        return (sum_a-sum_b)//2


    def findSwapValues(self,A, n, B, m):
        # Your code goes here
        A.sort()
        B.sort()

        i=0
        j=0

        target = self.getTarget(A,B)

        if target==float('-inf'):
            return -1

        while(i<n and j<m):
            diff=A[i]-B[j]
            if diff == target:
                return 1
            elif diff<target:
                i+=1
            else:
                j+=1
        return -1

s=Solution()
print(s.findSwapValues([1,2,3,4], 4, [1,2,3,4], 4))