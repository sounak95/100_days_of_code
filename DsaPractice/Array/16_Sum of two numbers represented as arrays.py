
# https://practice.geeksforgeeks.org/problems/sum-of-two-numbers-represented-as-arrays3110/1


class Solution:

    def findSum(self,a,b):
        n=len(a)
        m=len(b)
        k = max(m,n)
        output= [0] * k

        i=n-1
        j=m-1
        k=k-1
        carry=0
        while(i>=0 and j>=0):
            res = a[i] + b[j] + carry
            val = res%10
            carry = res//10
            output[k] = val
            i-=1
            j-=1
            k-=1

        while(i>=0):
            res = a[i] + carry
            val = res%10
            carry= res//10
            output[k] = val
            k-=1
            i-=1

        while(j>=0):
            res = b[j] + carry
            val = res%10
            carry = res//10
            output[k] = val
            k-=1
            j-=1

        if carry:
            output.insert(0,carry)

        return output

s=Solution()
s.findSum([2, 2, 7, 5, 3, 3], [4, 3, 3, 8])



