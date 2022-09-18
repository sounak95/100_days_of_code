
class Student:
    def __init__(self):
        print("const. invoked")

    def sun(self, a=None, b=None, c=None):
        if a and b and c:
            return a+ b +c
        elif a and b:
            return a + b
        else:
            return a


s=Student()
print(s.sun(1,2,3))
print(s.sun(1,2))
print(s.sun(1))


class B:

    def show(self):
        print("B of show")

class A(B):
    def show(self):
        print("A of show")

a=A()
a.show()
