

# https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def travarseLeft(self, root, ans):
        if (root is None) or (root.left is None and root.right is None):
            return
        ans.append(root.data)
        if root.left:
            self.travarseLeft(root.left, ans)
        else:
            self.travarseLeft(root.right, ans)

    def travarseLeaf(self, root, ans):
        if root is None:
            return

        if root.left is None and root.right is None:
            ans.append(root.data)
            return

        self.travarseLeaf(root.left, ans)
        self.travarseLeaf(root.right, ans)

    def travarseRight(self, root, ans):
        if (root is None) or (root.left is None and root.right is None):
            return
        if root.right:
            self.travarseRight(root.right, ans)
        else:
            self.travarseRight(root.left, ans)

        ans.append(root.data)

    def printBoundaryView(self, root):
        # Code here
        ans = []
        ans.append(root.data)
        self.travarseLeft(root.left, ans)

        self.travarseLeaf(root.left, ans)
        self.travarseLeaf(root.right, ans)

        self.travarseRight(root.right, ans)

        return ans