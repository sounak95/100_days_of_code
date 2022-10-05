

# https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1

import queue

import queue
class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return
        q = queue.Queue()
        q.put(root)
        l1 = []

        leftToRight= True
        while (not q.empty()):
            size = q.qsize()
            l2=[None]*size
            # level wise travarse
            for i in range(q.qsize()):
                currentNode = q.get()
                if not leftToRight:
                    index= size-i-1
                else:
                    index = i
                l2[index] = currentNode.data


                if currentNode.left:
                    q.put(currentNode.left)
                if currentNode.right:
                    q.put(currentNode.right)

            # l1.append(l2)
            l1.extend(l2)
            leftToRight = not leftToRight
        # print()
        # print(l1)
        return l1

