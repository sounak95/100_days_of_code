
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


def print_ll(head):
    while head is not None:
        print(str(head.data) + "->", end='')
        head=head.next
    print(None)
    return


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

def takeInput1():
    inputList=[int(ele) for ele in input().split()]
    head=None
    tail=None
    for currentData in inputList:
        if currentData==-1:
            break
        newNode= Node(currentData)
        if head is None:
            head=newNode
            tail=newNode
        else:
            tail.next=newNode
            tail=newNode
    return head


head=takeInput1()
# print(head)
print_ll(head)