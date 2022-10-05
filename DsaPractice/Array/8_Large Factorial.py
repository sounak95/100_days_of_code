
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/large-factorial4721

#User function Template for python3
class Solution:

    def fact(self, num):
        f=1
        for i in range(1,num+1):
            f*=i
        return f

    def factorial(self,a, n):
    # code here
        fact={}
        fact[0]=1
        MAX = pow(10,5)
        mod = pow(10,9) +7
        for i in range(1,MAX+1):
            fact[i] = (i * fact[i-1]) % mod

        for i,ele in enumerate(a):
            a[i] = fact[ele]

        return a

s=Solution()
print(s.fact(5))
print(s.factorial([0, 1, 2, 3, 4],5))
