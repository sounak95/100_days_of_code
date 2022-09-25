
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
