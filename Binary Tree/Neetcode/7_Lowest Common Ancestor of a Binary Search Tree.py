

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        curr = root

        while(curr):
            if p.val<curr.val and q.val<curr.val:
                curr= curr.left
            elif p.val>curr.val and q.val>curr.val:
                curr=curr.right
            else:
                return curr
