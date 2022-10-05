

# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-trees/problem/sum-tree

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:

    def issumTreeFast(self, root):
        if root is None:
            return True,0
        if root.left == None and root.right==None:
            return True, root.data
        isSumLeft, leftSum = self.issumTreeFast(root.left)
        isSumRight, rightSum = self.issumTreeFast(root.right)

        if root.data !=leftSum + rightSum:
            return False, 0
        if isSumLeft and isSumRight:
            return True, root.data + leftSum + rightSum
        else:
            return False, 0

    def isSumTree(self,root):
        # Code here
        return self.issumTreeFast(root)[0]

