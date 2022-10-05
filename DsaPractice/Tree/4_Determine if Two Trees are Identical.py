
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-trees/problem/determine-if-two-trees-are-identical

class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.data!=root2.data:
            return False
        return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)