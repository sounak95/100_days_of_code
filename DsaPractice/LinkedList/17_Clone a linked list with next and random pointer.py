

# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-linkedlist/problem/clone-a-linked-list-with-next-and-random-pointer

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None


class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        oldToCopy ={None:None}

        curr=head
        while(curr):
            oldToCopy[curr] = Node(curr.data)
            curr=curr.next

        curr=head
        while(curr):
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.arb = oldToCopy[curr.arb]
            curr=curr.next

        return oldToCopy[head]
