
class Student:
    def __init__(self, m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1= self.m1 + other.m1
        m2= self.m2 +other.m2

        return Student(m1,m2)

    def __gt__(self, other):
        r1= self.m1+ self.m2
        r2 = other.m1 +other.m2
        if r1>r2:
            return True
        return False

    def __str__(self):
        return f"m1:{self.m1} m2:{self.m2}"

s1 = Student(58,69)
s2 = Student(69,65)

s3=s1+s2
print(s3)

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")