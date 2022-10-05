

# https://practice.geeksforgeeks.org/problems/reorder-list/1



#User function Template for python3

'''
# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''

'''
# Linked List Class

'''

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def reorderList(self):
        if (self.head==None or self.head.next==None):
            return
        slow=fast = self.head

        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next

        curr=slow.next
        slow.next=prev=None

        while(curr):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next

        first,second= self.head,prev

        while(second):
            tmp1,tmp2= first,second
            first.next=second
            second.next=tmp1
            first,second= tmp1,tmp2

        return self.head
        # write code to reorder Nodes of Linked_List


#{
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

    def reorderList(self):
        if (self.head == None or self.head.next == None):
            return
        slow = fast = self.head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = prev = None

        while (curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        first, second = self.head, prev

        while (second):
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return self.head
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        lis.reorderList()
        lis.printList()

# } Driver Code Ends
