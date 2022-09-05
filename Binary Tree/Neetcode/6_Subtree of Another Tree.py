

# https://leetcode.com/problems/subtree-of-another-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def sameTree(self,s,t):
        if not s and not t:
            return True
        if s and t and s.val==t.val:
            return self.sameTree(s.left,t.left) and self.sameTree(s.right, t.right)

        return False

    def isSubtree(self, s, t):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        if not s:
            return False
        if self.sameTree(s,t):
            return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
