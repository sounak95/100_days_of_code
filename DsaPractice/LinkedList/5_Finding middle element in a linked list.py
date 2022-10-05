

# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-linkedlist/problem/finding-middle-element-in-a-linked-list

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

    def findMid(self, head):
        slow=fast=head

        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow.data
# Code here
# return the value stored in the middle node