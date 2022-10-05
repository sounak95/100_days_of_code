

# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-linkedlist/problem/delete-without-head-pointer

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        #code here
        # temp = curr_node.next
        curr_node.data = curr_node.next.data
        curr_node.next = curr_node.next.next
