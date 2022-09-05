
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder)==0:
            return None
        rootData= preorder[0]
        root = TreeNode(rootData)
        rootIndex=-1
        for i, ele in enumerate(inorder):
            if ele == rootData:
                rootIndex=i
                break
        if rootIndex==-1:
            return None
        leftInorder = inorder[:rootIndex]
        rightInorder =inorder[rootIndex+1:]

        lenLeftSubtree = len(leftInorder)

        leftPreorder = preorder[1:lenLeftSubtree+1]
        rightPreorder = preorder[lenLeftSubtree+1:]

        leftChild = self.buildTree(leftPreorder, leftInorder)
        rightChild = self.buildTree(rightPreorder, rightInorder)

        root.left = leftChild
        root.right = rightChild

        return root
