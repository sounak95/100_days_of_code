'''
Dequeue
Send Feedback
You need to implement a class for Dequeue i.e. for double ended queue. In this queue, elements can be inserted and deleted from both the ends.
You don't need to double the capacity.
You need to implement the following functions -
1. constructor
You need to create the appropriate constructor. Size for the queue passed is 10.
2. insertFront -
This function takes an element as input and insert the element at the front of queue. Insert the element only if queue is not full. And if queue is full, print -1 and return.
3. insertRear -
This function takes an element as input and insert the element at the end of queue. Insert the element only if queue is not full. And if queue is full, print -1 and return.
4. deleteFront -
This function removes an element from the front of queue. Print -1 if queue is empty.
5. deleteRear -
This function removes an element from the end of queue. Print -1 if queue is empty.
6. getFront -
Returns the element which is at front of the queue. Return -1 if queue is empty.
7. getRear -
Returns the element which is at end of the queue. Return -1 if queue is empty.
Input Format:
For C++ and Java, input is already managed for you. You just have to implement given functions.

For Python:
The choice codes and corresponding input for each choice are given in a new line. The input is terminated by integer -1. The following table elaborately describes the function, their choice codes and their corresponding input -
Alt Text

Output Format:
For C++ and Java, output is already managed for you. You just have to implement given functions.

For Python:
The output format for each function has been mentioned in the problem description itself.
Sample Input 1:
5 1 49 1 64 2 99 5 6 -1
Sample Output 1:
-1
64
99
Explanation:
The first choice code corresponds to getFront. Since the queue is empty, hence the output is -1.
The following input adds 49 at the top and the resultant queue becomes: 49.
The following input adds 64 at the top and the resultant queue becomes: 64 -> 49
The following input add 99 at the end and the resultant queue becomes: 64 -> 49 -> 99
The following input corresponds to getFront. Hence the output is 64.
The following input corresponds to getRear. Hence the output is 99.
'''

class Deque:
    def __init__(self):
        self.items = []
        self.max_len=10

    def isEmpty(self):
        return self.items == []

    def insertRear(self, item):
        if self.size()==self.max_len:
            return -1
        self.items.append(item)

    def insertFront(self, item):
        if self.size()==self.max_len:
            return -1
        self.items.insert(0, item)

    def deleteFront(self):
        if self.size()==0:
            return -1
        element= self.items.pop(0)
        return element


    def deleteRear(self):
        if self.size()==0:
            return -1
        element = self.items.pop()
        return element

    def getFront(self):
        if self.size()==0:
            return -1
        return self.items[0]

    def getRear(self):
        if self.size()==0:
            return -1
        return self.items[-1]

    def size(self):
        return len(self.items)

arr = [str(ele) for ele in input().split()]

# print(arr)
i=0
d=Deque()
while(i<len(arr)-1):
    if arr[i]=='1':
        ele = d.insertFront(arr[i+1])
        if ele==-1:
            print(ele)
        i+=2
    elif arr[i]=='2':
        ele = d.insertRear(arr[i+1])
        if ele==-1:
            print(ele)
        i+=2
    elif arr[i]=='3':
        ele =d.deleteFront()
        if ele==-1:
            print(ele)
        i+=1
    elif arr[i]=='4':
        ele =d.deleteRear()
        if ele==-1:
            print(ele)
        i+=1
    elif arr[i]=='5':
        print(d.getFront())
        i+=1
    elif arr[i]=='6':
        print(d.getRear())
        i+=1



