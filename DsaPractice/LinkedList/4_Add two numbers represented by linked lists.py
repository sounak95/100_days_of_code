

# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-linkedlist/problem/add-two-numbers-represented-by-linked-lists

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    #Function to add two numbers represented by linked list.

    def reverse(self, head):
        curr= head
        prev=None
        while(curr):
            next= curr.next
            curr.next = prev
            prev= curr
            curr =next
        return prev

    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        first = self.reverse(first)
        second = self.reverse(second)

        dummyNode = Node(0)
        tail=dummyNode
        carry=0
        while(first or second or carry):
            val1 = first.data if first else 0
            val2 = second.data if second else 0
            val = val1+val2+carry
            carry = val//10
            val= val%10
            newNode = Node(val)
            tail.next = newNode

            tail=tail.next
            first = first.next if first else None
            second = second.next if second else None

        return self.reverse(dummyNode.next)

