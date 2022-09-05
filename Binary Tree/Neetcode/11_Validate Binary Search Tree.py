
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkBst(self, root):
        if not root:
            return float('inf'), float('-inf'), True
        leftMin, leftMax, isLeftBalanced = self.checkBst(root.left)
        rightMin, rightMax, isRightBalanced = self.checkBst(root.right)

        minimum = min(root.val, leftMin, rightMin)
        maximum = max(root.val, rightMax, leftMax)

        isBalanced = True

        # print( rightMin<root.val)
        if leftMax >= root.val or rightMin <= root.val:
            isBalanced = False

        if (not isLeftBalanced) or (not isRightBalanced):
            isBalanced = False

        return minimum, maximum, isBalanced

    def isValidBST(self, root):
        min, max, isBst = self.checkBst(root)
        return isBst
