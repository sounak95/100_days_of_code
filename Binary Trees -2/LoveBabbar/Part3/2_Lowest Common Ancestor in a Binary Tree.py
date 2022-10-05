

# https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        # Code here
        if root is None:
            return None
        if root.data==n1 or root.data ==n2:
            return root

        leftAns = self.lca(root.left, n1,n2)
        rightAns = self.lca(root.right, n1, n2)

        if leftAns and rightAns:
            return root

        elif leftAns and not rightAns:
            return leftAns
        elif rightAns and not leftAns:
            return rightAns
        else:
            return None
