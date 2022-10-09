# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-linkedlist/problem/intersection-point-in-y-shapped-linked-lists

# User function Template for python3



# Function to find intersection point in Y shaped Linked Lists.
def getLength(head):
    temp = head
    count = 0

    while (temp):
        count += 1
        temp = temp.next

    return count


def utility(d, head1, head2):
    i = 0
    current1 = head1
    while (i < d):
        if current1 is None:
            return -1
        current1 = current1.next
        i += 1

    current2 = head2
    while (current1 and current2):
        if current1 is current2:
            return current1.data
        # print("******")
        # print(current1.data, current2.data)
        current1 = current1.next
        current2 = current2.next

    return -1


def intersetPoint(head1, head2):
    # code here
    c1 = getLength(head1)
    c2 = getLength(head2)

    if c1 > c2:
        d = c1 - c2
        # print(d)
        return utility(d, head1, head2)
    else:
        d = c2 - c1
        # print(d)
        return utility(d, head2, head1)


# {
# Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        temp = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        x, y, z = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node = Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node = Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node = Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i == 0:
                b.append(node)  # add to the end of the list b, only the intersection

        print(intersetPoint(a.head, b.head))

# } Driver Code Ends