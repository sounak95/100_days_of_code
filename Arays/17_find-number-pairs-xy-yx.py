"""
Find number of pairs (x, y) in an array such that x^y > y^x

Input
10 19 18
11 15 9
Output:
10 11
10 15
2

"""

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

count=0
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if pow(arr1[i], arr2[j])>pow(arr2[j], arr1[i]):
            print(arr1[i],arr2[j])
            count+=1
print(count)

