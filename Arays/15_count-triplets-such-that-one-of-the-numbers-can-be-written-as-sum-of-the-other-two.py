"""
Count Triplets such that one of the numbers can be written as sum of the other two
Given an array A[] of N integers. The task is to find the number of triples (i, j, k) , where i, j, k are indices and (1 <= i < j < k <= N), such that in the set { A_i, A_j, A_k} at least one of the numbers can be written as the sum of the other two.

Examples:

Input : A[] = {1, 2, 3, 4, 5}
Output : 4
The valid triplets are:
(1, 2, 3), (1, 3, 4), (1, 4, 5), (2, 3, 5)

Input : A[] = {1, 1, 1, 2, 2}
Output : 6


"""

arr = list(map(int,input().split()))
n= len(arr)
count=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1, n):
            if arr[i]==arr[j]+arr[k] or arr[j]== arr[i]+arr[k] or arr[k]==arr[i]+arr[j]:
                # print(arr[i],arr[j],arr[k])
                count+=1
print(count)
