

# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def getHeightAndCheckBalanced(self, root):
        if root is None:
            return 0, True

        lh, isBalancedLeft = self.getHeightAndCheckBalanced(root.left)
        rh, isBalancedRight = self.getHeightAndCheckBalanced(root.right)
        h = 1 + max(lh, rh)
        isBalanced = True

        if lh - rh > 1 or rh - lh > 1:
            isBalanced = False

        # if isBalanced:
        #     if isBalancedLeft and isBalancedRight:
        #         isBalanced = True
        #     else:
        #         isBalanced = False

        if not isBalancedLeft or not isBalancedRight:
            isBalanced=False

        return h, isBalanced

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        h, isBalanced = self.getHeightAndCheckBalanced(root)
        return isBalanced
