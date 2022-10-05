
# https://practice.geeksforgeeks.org/problems/square-root/1

# https://leetcode.com/problems/sqrtx/

class Solution(object):

    def morePrecision(self, n, precision, tempSol):
        ans= tempSol
        factor =1
        for i in range(precision):
            factor = factor/10

            j=ans
            while((j*j)<n):
                ans= j
                j=round(j+factor, precision)
        return ans


    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=0
        e= x
        m = s+(e-s)//2
        ans=-1
        while(s<=e):
            square = m*m
            if square==x:
                return m
            if square<x:
                ans= m
                s=m+1
            else:
                e=m-1

            m = s+(e-s)//2
        return self.morePrecision(x,3, ans )

s=Solution()
print(s.mySqrt(82))


