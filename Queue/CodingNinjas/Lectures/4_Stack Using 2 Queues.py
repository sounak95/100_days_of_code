from sys import stdin


class Stack:
    # Define data members and __init__()

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):

    # Implement the getSize() function

    def isEmpty(self):

    # Implement the isEmpty() function

    def push(self, data):

    # Implement the push(element) function

    def pop(self):

    # Implement the pop() function

    def top(self):


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