
class BinaryTreeNode:
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None

b1 = BinaryTreeNode(1)
b2 = BinaryTreeNode(2)
b3 = BinaryTreeNode(3)

b1.left = b2
b1.right = b3
