
# https://practice.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1


# User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''


class Solution:

    def __init__(self):
        self.maxSum = float('-inf')
        self.maxLen = 0

    def solve(self, root, sum, len):
        if root is None:
            if len > self.maxLen:
                self.maxLen = len
                self.maxsum = sum
            elif len == self.maxLen:
                self.maxsum = max(sum, self.maxsum)
            return

        sum = sum + root.data

        self.solve(root.left, sum,  len + 1)
        self.solve(root.right, sum,  len + 1)

    def sumOfLongRootToLeafPath(self, root):
        # code here
        sum = 0

        len = 0

        self.solve(root, sum,  len)
        return self.maxsum


# {
# Driver Code Starts
# Initial Template for Python 3

from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = input()
        root = buildTree(s)
        ob = Solution()
        res = ob.sumOfLongRootToLeafPath(root)
        print(res)
# } Driver Code Ends