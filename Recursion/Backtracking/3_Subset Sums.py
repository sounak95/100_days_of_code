
# https://practice.geeksforgeeks.org/problems/subset-sums2234/1


class Solution:

    def func(self, ind, sum, arr,ans ):
        if ind==len(arr):
            ans.append(sum)
            return

        self.func(ind+1, sum+arr[ind] , arr, ans)
        self.func(ind + 1, sum , arr, ans)


    def subsetSums(self, arr, N):
        # code here
        ans=[]
        sum=0
        self.func(0,sum,arr, ans)
        return sorted(ans)