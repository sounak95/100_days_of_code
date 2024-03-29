
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-trees/problem/height-of-binary-tree

class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if root is None:
            return 0
        return 1 + max(self.height(root.left) , self.height(root.right))

