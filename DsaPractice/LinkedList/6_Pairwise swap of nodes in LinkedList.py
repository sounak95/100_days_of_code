
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-linkedlist/problem/pairwise-swap-of-nodes-in-linkelist

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

    def pairwiseSwap(head):

        temp=head

        while(temp and temp.next):
            temp.data,temp.next.data = temp.next.data, temp.data

            temp=temp.next.next
        return head
# code here