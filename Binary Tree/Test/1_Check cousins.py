'''
Check cousins
Send Feedback
Given the binary Tree and two nodes say ‘p’ and ‘q’. Determine whether the two nodes are cousins of each other or not. Two nodes are said to be cousins of each other if they are at same level of the Binary Tree and have different parents.
Do it in O(n).
Input format :
Line 1 : Nodes in level order form (separated by space). If any node does not have left or right child, take -1 in its place
Line 2 : integer value of p
Line 3 : Integer value of q
Output format :
true or false
Constraints :
1 <= N <= 10^5
Sample Input :
5 6 10 2 3 4 -1 -1 -1 -1 9 -1 -1 -1 -1
2
4
Sample Output :
true
'''



import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSibling(root, a, b):
    if root is None:
        return False

    if (root.left is not None and root.left.data ==a and root.right is not None and root.right.data==b) or (root.left is not None and root.left.data ==b and root.right is not None and  root.right.data ==a):
        return True
    return isSibling(root.left, a,b) or isSibling(root.right, a,b)


def get_level(root,data,level=1):
    if root is None:
        return 0
    if root.data ==data:
        return level

    check_level_left_sub_tree = get_level(root.left,data,level+1)

    if check_level_left_sub_tree!=0:
        return check_level_left_sub_tree

    check_level_right_sub_tree = get_level(root.right, data, level+1)
    return check_level_right_sub_tree

def checkCousins(root,p,q):
    #Implement Your Code Here
    if get_level(root,p) == get_level(root,q) and not(isSibling(root,p,q)):
        return True
    return False

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
p = int(input())
q = int(input())
ans = checkCousins(root,p,q)
if ans is True:
    print('true')
else:
    print('false')