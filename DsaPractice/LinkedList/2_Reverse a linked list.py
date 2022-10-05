
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        prev=None
        curr= head
        while(curr):
            next = curr.next
            curr.next = prev
            prev= curr
            curr = next
        return prev
