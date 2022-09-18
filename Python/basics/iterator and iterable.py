
nums=[1,2,3,4,5,6,7,8,9]

it = iter(nums)
print(it.__next__())
print(next(it))

class TopTen:
    def __init__(self):
        self.num =1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num+=1
            return val
        else:
            raise StopIteration

it = iter(TopTen())
print(it.__next__())
print(next(it))
print(next(it))

values = TopTen()
for i in values:
    print(i)



