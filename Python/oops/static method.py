
class Student:
    school_name ="telusko"
    def __init__(self,m1):
        self.m1=m1

    def get_m1(self):
        return self.m1

    @classmethod
    def getSchool(cls):
        return cls.school_name

    @staticmethod
    def getInfo():
        return "abc"

print(Student.getSchool())
print(Student.getInfo())

