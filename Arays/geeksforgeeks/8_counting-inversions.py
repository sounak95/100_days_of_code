# https://www.geeksforgeeks.org/counting-inversions/

def getInvCount(arr, n):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                count+=1
    return count

arr = [1, 20, 6, 4, 5]
n = len(arr)
print("Number of inversions are",
      getInvCount(arr, n))
