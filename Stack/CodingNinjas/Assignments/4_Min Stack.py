

# https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        self.__st = []
        self.__minSt = []

    def push(self, val: int) -> None:
        self.__st.append(val)
        if self.__minSt:
            val = min(self.__minSt[-1], val)
        self.__minSt.append(val)

    def pop(self) -> None:
        if self.__st:
            self.__st.pop()
            self.__minSt.pop()

    def top(self) -> int:
        if self.__st:
            return self.__st[-1]

    def getMin(self) -> int:
        return self.__minSt[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()