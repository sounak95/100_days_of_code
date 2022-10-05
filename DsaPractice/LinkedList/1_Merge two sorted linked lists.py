
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-linkedlist/problem/merge-two-sorted-linked-lists

# User function Template for python3

	# Function to merge two sorted lists in one
	# using constant space.
    #
	# Function Arguments: head_a and head_b (head reference of both the sorted lists)
	# Return Type: head of the obtained list after merger.
    #
	# {
		# Node Class

	# }

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


# Function to merge two sorted linked list.
def sortedMerge(head1, head2):
    # code here
    dummyNode = Node(0)
    tail = dummyNode

    while (head1 and head2):
        if head1.data < head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1

    if head2:
        tail.next = head2

    return dummyNode.next
