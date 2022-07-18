
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

q=QueueUsingArray()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

while(not q.isEmpty()):
    print(q.front())
    q.dequeue()

print(q.dequeue())