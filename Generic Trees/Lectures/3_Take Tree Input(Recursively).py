class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def printTree(root):
    # TNot a base case
    if root == None:
        return
    print(root.data)
    for child in root.children:
        printTree(child)


def printTreeDetailed(root):
    if root == None:
        return

    print(root.data, ":", end="")
    for child in root.children:
        print(child.data, ",", end="")
    print()

    for child in root.children:
        printTreeDetailed(child)

def takeTreeInput():
    print('Enter root data')
    rootData = int(input())
    if rootData ==-1:
        return
    root = TreeNode(rootData)
    print('Enter the number of children for', rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child=takeTreeInput()
        root.children.append(child)
    return root

root=takeTreeInput()
printTreeDetailed(root)
