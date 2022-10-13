'''
A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
'''
# https://www.youtube.com/watch?v=SgUwPDT9tEs
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

lst1 =[[1,0,0],[2,1,3],[3,4,5]]
lst2= lst1.copy()
lst1[1][0]=100
print(lst1)
print(lst2)

import copy

lst1 =[[1,0,0],[2,1,3],[3,4,5]]
lst2= copy.deepcopy(lst1)
lst1[1][0]=100
print(lst1)
print(lst2)
