

# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        self.__s1=[]
        self.__s2=[]

    def push(self, x: int) -> None:

        while(len(self.__s1)!=0):
            self.__s2.append(self.__s1.pop())

        self.__s1.append(x)

        while(len(self.__s2)!=0):
            self.__s1.append(self.__s2.pop())


    def pop(self) -> int:
        if not self.empty():
            return self.__s1.pop()

    def peek(self) -> int:
        if not self.empty():
            return self.__s1[-1]


    def empty(self) -> bool:
        return len(self.__s1)==0
