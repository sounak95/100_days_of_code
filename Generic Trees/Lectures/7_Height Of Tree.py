'''
Height Of Tree
Send Feedback
Given a generic tree, find and return the height of given tree.
Input Format:
The first line of input contains data of the nodes of the tree in level order form. The order is: data for root node, number of children to root node, data of each of child nodes and so on and so forth for each node. The data of the nodes of the tree is separated by space.
Output Format :
The first and only line of output prints the height of the given generic tree.
Constraints:
Time Limit: 1 sec
Sample Input 1:
10 3 20 30 40 2 40 50 0 0 0 0
Sample Output 1:
3
'''

import sys
import queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def inputLevelWise(li):
    i = 0
    data = li[i]
    i += 1
    if data == -1:
        return None
    root = TreeNode(data)
    q = queue.Queue()
    q.put(root)
    while (not q.empty()):
        frontNode = q.get()
        noOfChildren = li[i]
        i += 1
        childrenArray = li[i: i + noOfChildren]
        for childData in childrenArray:
            childNode = TreeNode(childData)
            frontNode.children.append(childNode)
            q.put(childNode)
        i = i + noOfChildren
    return root


def heightOfTree(root):
    if root == None:
        return 0
    height = 0
    for child in root.children:
        height=max(heightOfTree(child), height)
    return height +1


# main
sys.setrecursionlimit(10 ** 6)
li = [int(elem) for elem in list(input().strip().split())]
root = inputLevelWise(li)
print(heightOfTree(root))