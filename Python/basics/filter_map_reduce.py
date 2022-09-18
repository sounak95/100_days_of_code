
nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda x:x%2==0, nums))
print(evens)

doubles = list(map(lambda x:x*2, nums))
print(doubles)

from functools import reduce
sum = reduce(lambda a,b:a+b, nums)
print(sum)