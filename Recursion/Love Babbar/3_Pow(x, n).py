import sys
sys.setrecursionlimit(10**6)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # print(n)
        if n==0:
            return 1
        if n==1:
            return x

        ans = self.myPow(x, n//2)

        if n%2==0:
            return ans * ans
        else:
            return x * ans * ans