
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

def length(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count

def insert_at_i(head,i,data):
    if i<0 or  i>length(head):
        return head
    count=0
    prev=None
    curr=head
    newNode=Node(data)
    while(count<i):
        prev=curr
        curr=curr.next
        count+=1

    if prev is not None:
        prev.next=newNode
    else:
        head=newNode
    newNode.next=curr
    return head


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
print_ll(head)
head=insert_at_i(head,2,6)
print_ll(head)
head=insert_at_i(head,0,9)
print_ll(head)
head=insert_at_i(head,8,10)
print_ll(head)