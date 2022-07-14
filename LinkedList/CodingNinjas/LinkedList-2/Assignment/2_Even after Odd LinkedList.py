'''
Even after Odd LinkedList
Send Feedback
For a given singly linked list of integers, arrange the elements such that all the even numbers are placed after the odd numbers. The relative order of the odd and even terms should remain unchanged.
Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format:
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first line of each test case or query contains the elements of the singly linked list separated by a single space.
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format:
For each test case/query, print the elements of the updated singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Where M is the size of the singly linked list.

Time Limit: 1sec
Sample Input 1 :
1
1 4 5 2 -1
Sample Output 1 :
1 5 4 2
Sample Input 2 :
2
1 11 3 6 8 0 9 -1
10 20 30 40 -1
Sample Output 2 :
1 11 3 9 6 8 0
10 20 30 40
'''

from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def evenAfterOdd(head):
    odd_head=odd_tail=even_head=even_tail = None

    while head!=None:
        if head.data%2!=0:
            if odd_head is None:
                odd_head = head
                odd_tail = head
            else:
                odd_tail.next = head
                odd_tail = head
        elif head.data%2 ==0:
            if even_head is None:
                even_head = head
                even_tail = head
            else:
                even_tail.next = head
                even_tail = head
        head=head.next

    if even_tail is not None:
        even_tail.next = None

    if odd_tail is not None:
        odd_tail.next = None
        odd_tail.next = even_head

    if odd_head is not None:
        return odd_head

    return even_head

# Your code goes here


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)

    t -= 1