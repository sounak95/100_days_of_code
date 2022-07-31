
class BinaryTreeNode:
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None

def printTree(root):
    if root ==None:
        return
    print(root.data)
    printTree(root.left)
    printTree(root.right)



def printDetailedTree(root):
    if root ==None:
        return
    print(root.data , end=":")
    if root.left !=None:
        print(f"L: {root.left.data}", end=',')
    if root.right!=None:
        print(f"R: {root.right.data}", end='')
    print()
    printDetailedTree(root.left)
    printDetailedTree(root.right)

def treeInput():
    rootData= int(input())
    if rootData==-1:
        return None
    root = BinaryTreeNode(rootData)
    leftTree=treeInput()
    rightTree=treeInput()
    root.left = leftTree
    root.right = rightTree
    return root


def removeLeaves(root):
    if root ==None:
        return None
    if root.left ==None and root.right ==None:
        return None

    root.left = removeLeaves(root.left)
    root.right = removeLeaves(root.right)

    return root

root=treeInput()
printDetailedTree(root)
root=removeLeaves(root)
printDetailedTree(root)


