from sys import stdin

class QueueUsingArray:
    def __init__(self):
        self.__arr=[]
        self.__count=0
        self.__front=0

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size()==0

    def enqueue(self, data):
        self.__arr.append(data)
        self.__count+=1

    def dequeue(self):
        if self.isEmpty():
            return -1
        element= self.__arr[self.__front]
        self.__front+=1
        self.__count-=1
        return element

    def front(self):
        if self.isEmpty():
            return -1
        return self.__arr[self.__front]

class Stack:
    # Define data members and __init__()
    def __init__(self):
        self.__q1 = QueueUsingArray()
        self.__q2 = QueueUsingArray()
    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
        return self.__q1.size()
    # Implement the getSize() function

    def isEmpty(self):
        return self.__q1.isEmpty()
    # Implement the isEmpty() function

    def push(self, data):
        self.__q2.enqueue(data)
        while(not self.__q1.isEmpty()):
            data = self.__q1.front()
            self.__q2.enqueue(self.__q1.dequeue())
        self.__q1, self.__q2= self.__q2, self.__q1
    # Implement the push(element) function

    def pop(self):
        return self.__q1.dequeue()
    # Implement the pop() function

    def top(self):
        return self.__q1.front()


# Implement the top() function


# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1