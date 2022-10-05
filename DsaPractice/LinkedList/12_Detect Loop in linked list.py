

# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-linkedlist/problem/detect-loop-in-linked-list


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # code here
        slow = fast = head
        while (fast and fast.next):

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

