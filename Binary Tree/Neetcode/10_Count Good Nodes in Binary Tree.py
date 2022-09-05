
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root):
        def dfs(root, max_val):
            if not root:
                return 0
            res=1 if root.val>=max_val else 0
            max_val = max(root.val, max_val)

            return res+ dfs(root.left, max_val) + dfs(root.right, max_val)
        return dfs(root, root.val)
