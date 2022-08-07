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
        return float('inf')
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(root.data, leftMin, rightMin)

def maxTree(root):
    if root==None:
        return float('inf')
    leftMax = maxTree(root.left)
    rightMax = minTree(root.right)
    return max(maxTree.data, leftMax, rightMax)

def isBst(root):
    if root==None:
        return True
    leftMax = maxTree(root.left)
    rightMin = minTree(root.right)

    if root.data<=leftMax or root.data>rightMin:
        return False
    isLeftBst = isBst(root.left)
    isRightBst = isBst(root.right)

    return isLeftBst and isRightBst

root=takeTreeInputLevelWise()
printTreeDetailed(root)
isBst(root)
