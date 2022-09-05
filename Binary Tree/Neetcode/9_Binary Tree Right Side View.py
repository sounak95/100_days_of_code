
# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
import queue


class Solution(object):
    def rightSideView(self, root):
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
                    l1.append(l2[-1])
                    l2 = []
        l1.append(l2[-1])
        print()
        print(l1)
        return l1