

# https://leetcode.com/problems/binary-tree-level-order-traversal/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# https://leetcode.com/problems/binary-tree-level-order-traversal/

import queue


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return
        q = queue.Queue()
        q.put(root)

        q.put(None)
        l1 = []
        l2 = []
        while (not q.empty()):
            currentNode = q.get()
            if currentNode is not None:
                print(currentNode.val, end=' ')
                l2.append(currentNode.val)
                if currentNode.left is not None:
                    q.put(currentNode.left)
                if currentNode.right is not None:
                    q.put(currentNode.right)
            else:
                if not (q.qsize() == 0):
                    q.put(None)
                    print()
                    l1.append(l2)
                    l2 = []
        l1.append(l2)
        print()
        print(l1)
        return l1

