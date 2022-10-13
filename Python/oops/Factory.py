

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def base_method(self):
        pass

class A(Base):
    def base_method(self):
        print(f"Base method of A")

class B(Base):
    def base_method(self):
        print(f"Base method of B")


class factory:
    @staticmethod
    def build_class(class_name):
        if class_name =='A':
            return A()
        elif class_name =='B':
            return B()


# A().base_method()
# B().base_method()

factory.build_class('A').base_method()
factory.build_class('B').base_method()


