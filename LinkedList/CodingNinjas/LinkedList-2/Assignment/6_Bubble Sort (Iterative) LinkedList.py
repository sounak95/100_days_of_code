'''
Bubble Sort (Iterative) LinkedList
Send Feedback
Given a singly linked list of integers, sort it using 'Bubble Sort.'
Note :
No need to print the list, it has already been taken care. Only return the new head to the list.
Input format :
The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
For each test case/query, print the elements of the sorted singly linked list.

Output for every test case will be printed in a seperate line.
Constraints :
0 <= M <= 10^3
Where M is the size of the singly linked list.

Time Limit: 1sec
Sample Input 1 :
10 9 8 7 6 5 4 3 -1
Sample Output 1 :
 3 4 5 6 7 8 9 10
 Sample Input 2 :
10 -5 9 90 5 67 1 89 -1
Sample Output 2 :
-5 1 5 9 10 67 89 90
'''

from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




def length(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count
#   p c f
# 1 3 5 2 6
#   p c f
# 1 3 2 5 6

# c f
# 3 2 1
# p c f
# 2 3 1
def bubbleSort(head) :
    n= length(head)
    # print(n)
    for i in range(n):
        prev= None
        curr = head

        for j in range(n-1-i):
            if curr.data<=curr.next.data:
                prev= curr
                curr= curr.next
            else:
                if prev is not None:
                    fwd = curr.next
                    prev.next = fwd
                    curr.next=fwd.next
                    fwd.next = curr
                    prev = fwd
                else:
                    fwd = curr.next
                    head=head.next
                    curr.next=fwd.next
                    fwd.next=curr
                    prev=fwd
    return head

































def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)