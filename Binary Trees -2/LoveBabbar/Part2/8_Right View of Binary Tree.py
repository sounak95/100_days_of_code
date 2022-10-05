
# https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1


class Solution:
    # Function to return list containing elements of right view of binary tree.

    def solve(self, root, ans, level):
        if root is None:
            return
        if level == len(ans):
            ans.append(root.data)

        self.solve(root.right, ans, level + 1)
        self.solve(root.left, ans, level + 1)

    def rightView(self, root):
        ans = []
        self.solve(root, ans, 0)
        return ans

# code here

