

def sumArray(arr):
    # Please add your code here
    if len(arr)==1:
        return arr[0]
    return arr[0]+sumArray(arr[1:])

def sumArray_1(arr, index):
    # Please add your code here
    if index==len(arr)-1:
        return arr[index]
    return arr[index]+sumArray_1(arr, index+1)

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
# print(sumArray(arr))
print(sumArray_1(arr,0))
