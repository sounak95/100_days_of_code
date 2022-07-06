
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def takeInput():
    inputList=[int(ele) for ele in input().split()]
    head=None
    for currentData in inputList:
        if currentData==-1:
            break
        newNode= Node(currentData)
        if head is None:
            head=newNode
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next= newNode
    return head


head=takeInput()
print(head)