
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-trees/problem/check-for-balanced-tree

class Solution:

    def height(self, root):
        # code here
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    # def isBalanced(self ,root):
    #     if root is None:
    #         return True
    #     lh = self.height(root.left)
    #     rh = self.height(root.right)
    #
    #     if abs(lh-rh)>1:
    #         return False
    #
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)


    def helper(self, root):
        if root is None:
            return 0, True

        lh, isLeftBalanced = self.helper(root.left)
        rh, isRightBalanced = self.helper(root.right)

        h = 1 + max(lh, rh)

        if abs(lh - rh) > 1:
            return h, False

        if isLeftBalanced and isRightBalanced:
            return h, True
        else:
            return h, False

    def isBalanced(self, root):
        a, b = self.helper(root)
        return b


# add code here

