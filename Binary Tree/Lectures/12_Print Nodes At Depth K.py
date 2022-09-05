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


def printDepthK(root,k):
    if root ==None:
        return
    if k==0:
        print(root.data)

    printDepthK(root.left, k-1)
    printDepthK(root.right, k-1)


def printDepthKV2(root,k, d):
    if root ==None:
        return
    if k==d:
        print(root.data)

    printDepthKV2(root.left, k, d+1)
    printDepthKV2(root.right, k, d+1)

root=treeInput()
printDetailedTree(root)
printDepthK(root,2)
printDepthKV2(root,2)