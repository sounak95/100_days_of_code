

# https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

def solve(root, ans, level):
    if root is None:
        return
    if level ==len(ans):
        ans.append(root.data)

    solve(root.left, ans, level+1)
    solve(root.right, ans, level+1)


def LeftView(root):
    ans=[]
    solve(root, ans, 0)
    return ans