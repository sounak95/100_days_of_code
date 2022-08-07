class BinaryTreeNode:
    def __init__(self,data):
        self.data=data;
        self.left=None
        self.right=None

def search(root,x):
    if root==None:
        return False
    if root.data==x:
        return True
    elif root.data>x:
        return search(root.left,x)
    else:
        return search(root.left,x)

def printTreeDetailed(root):
    if root==None:
        return
    print(root.data,end=":")
    if root.left!=None:
        print("L",root.left.data,end=",")
    if root.right!=None:
        print("R",root.right.data,end="")
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

import queue
def takeTreeInputLevelWise():
    q=queue.Queue()
    print("Enter root")
    rootData=int(input())
    if rootData==-1:
        return None
    root=BinaryTreeNode(rootData)
    q.put(root)
    while(not(q.empty())):
        current_node=q.get()
        print("Enter left child of",current_node.data)
        leftChildData=int(input())
        if leftChildData!=-1:
            leftChild=BinaryTreeNode(leftChildData)
            current_node.left=leftChild
            q.put(leftChild)
        print("Enter right child of",current_node.data)
        rightChildData=int(input())
        if rightChildData!=-1:
            rightChild=BinaryTreeNode(rightChildData)
            current_node.right=rightChild
            q.put(rightChild)
    return root

def minTree(root):
    if root==None:
        return 100000
    leftMin=minTree(root.left)
    rightMin=minTree(root.right)
    return min(leftMin,rightMin,root.data)

def maxTree(root):
    if root==None:
        return -100000
    leftMax=maxTree(root.left)
    rightMax=maxTree(root.right)
    return max(leftMax,rightMax,root.data)

def isBST2(root):
    if root==None:
        return float('inf') , float('-inf'), True
    leftMin, leftMax, isLeftBST = isBST2(root.left)
    rightMin, rightMax, isrightBST = isBST2(root.right)

    minimum = min(leftMin, rightMin, root.data)
    maximun = max(leftMax, rightMax, root.data)
    isTreeBST = True
    if root.data<=leftMax or root.data>rightMin:
        isTreeBST = False

    if not (isLeftBST) or not(isrightBST):
        isTreeBST = False

    return minimum, maximun, isTreeBST

