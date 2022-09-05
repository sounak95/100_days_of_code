
# https://leetcode.com/problems/diameter-of-binary-tree/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def heightAndDiameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if  root is None:
            return 0,0

        ld,lh = self.heightAndDiameterOfBinaryTree(root.left)
        rd,rh = self.heightAndDiameterOfBinaryTree(root.right)

        h = 1+ max(lh,rh)

        return max(lh+rh, ld,rd),h

    def diameterOfBinaryTree(self,root):
        d, h = self.heightAndDiameterOfBinaryTree(root)
        return d