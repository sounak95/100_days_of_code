
# https://leetcode.com/problems/subsets/

class Solution:

    def helper(self, arr, i, output, ans):
        # print(ans)
        if i >= len(arr):
            ans.append(output.copy())
            return

        # exclued
        self.helper(arr, i + 1, output, ans)

        # include
        output.append(arr[i])

        self.helper(arr, i + 1, output, ans)
        output.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        output = []
        self.helper(nums, 0, output, ans)
        return ans


s=Solution()
print(s.subsets([1,2,3]))

