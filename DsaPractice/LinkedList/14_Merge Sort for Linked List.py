
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-linkedlist/problem/sort-a-linked-list

# User function Template for python3

'''
    :param head: head of unsorted linked list
    :return: head of sorted linkd list

    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    # Function to sort the given linked list using Merge Sort.
    def findMid(self, head):
        if head is None :
            return head
        slow = fast = head

        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, lst1, lst2):
        dummyNode = Node(0)
        tail = dummyNode

        while (lst1 and lst2):
            if lst1.data < lst2.data:
                tail.next = lst1
                lst1=lst1.next
            else:
                tail.next = lst2
                lst2 = lst2.next

            tail = tail.next

        if lst1:
            tail.next = lst1

        if lst2:
            tail.next = lst2

        return dummyNode.next

    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        mid = self.findMid(head)

        lst1 = head
        lst2 = mid.next
        mid.next = None
        head1 = self.mergeSort(lst1)
        head2 = self.mergeSort(lst2)
        fHead = self.merge(head1, head2)
        return fHead


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node


# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList()  # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends