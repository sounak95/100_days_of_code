

# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-trees/problem/diameter-of-binary-tree

class Solution:
    def height(self, root):
        # code here
        if root is None:
            return 0
        return 1 + max(self.height(root.left) , self.height(root.right))
    # Function to return the diameter of a Binary Tree.

    def heightAndDiameter(self, root):
        if root is None:
            return 0,0
        lh,ld = self.heightAndDiameter(root.left)
        rh,rd = self.heightAndDiameter(root.right)
        h= 1+ max(lh,rh)
        return h, max(1+lh+rh, ld, rd)

    def diameter(self, root):
        return self.heightAndDiameter(root)[1]



# Code here
