

# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-linkedlist/problem/nth-node-from-end-of-linked-list

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


def getNthFromLast(head,n):
    dummyNode = Node(0)
    dummyNode.next = head

    left = dummyNode
    right = head

    while (n > 0):
        if not right:
            return -1
        right = right.next
        n -= 1


    while (right):
        right = right.next
        left = left.next

    return left.next.data

