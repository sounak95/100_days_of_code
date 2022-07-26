## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
    if head is None:
        return head
    prev=None
    curr=head
    while(curr is not None):
        next = curr.next
        curr.next = prev
        prev= curr
        curr=next
    Node = prev
    return Node

def nextNumber(head):
    # Implement Your Code here
    head = reverseList(head)
    prev=None
    curr=head
    curr.data+=1
    carry= 0

    while(curr is not None) and (curr.data>9 or carry>0):

        prev= curr
        curr.data= curr.data+carry
        carry = curr.data // 10
        curr.data= curr.data%10
        curr=curr.next

    if carry>0:
        prev.next = Node(carry)

    return reverseList(head)




def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next
    return


# Main
# Read the link list elements including -1
arr = [int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)