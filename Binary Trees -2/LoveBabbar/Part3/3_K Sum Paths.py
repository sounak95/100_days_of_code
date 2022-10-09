

# https://practice.geeksforgeeks.org/problems/k-sum-paths/1

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def __init__(self):
        self.count=0

    def solve(self, root, k, path):
        if not root:
            return
        path.append(root.data)

        self.solve(root.left,k, path)
        self.solve(root.right, k, path)

        sum=0
        for i in reversed(range(len(path))):
            sum+=path[i]
            if sum==k:
                self.count+=1
        path.pop()


    def sumK(self,root,k) :
        # code here
        path=[]
        self.solve(root,k,path )
        return self.count