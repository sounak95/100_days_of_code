
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/plus-one


class Solution:
    # def increment(self, arr, N):
    #     # code here
    #     res=0
    #     for ele in arr:
    #         res = res*10 + ele
    #
    #     return str(res+1)


    def increment(self, arr, N):
        # code here
        carry=1
        # temp=[0] *(N+1)
        for i in reversed(range(N)):
            res = arr[i]+ carry
            val = res%10
            carry = res//10
            arr[i] = val
        if carry:
            arr.insert(0,1)
        return arr

s=Solution()
print(s.increment([9,9,9],3))
print(s.increment([1,2,4],3))
