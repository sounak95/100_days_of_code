
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

import queue

def takeTreeInputLevelWise():
    q=queue.Queue()
    print("Enter root:")
    rootData = int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while(not q.empty()):
        currentNode = q.get()

        print("Enter left child of ", currentNode.data)
        leftChildData = int(input())
        if leftChildData!=-1:
            leftChild = BinaryTreeNode(leftChildData)
            currentNode.left = leftChild
            q.put(leftChild)

        print("Enter right child of ", currentNode.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            currentNode.right = rightChild
            q.put(rightChild)

    return root

root=takeTreeInputLevelWise()
printDetailedTree(root)