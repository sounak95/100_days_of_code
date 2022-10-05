# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/maximum-index3307


def maxIndexDiff(arr,n):
    res = float('-inf')
    for i in range(n):
        for j in range(i, n):
            if arr[j]>=arr[i]:
                diff = j-i
                res = max(diff, res)
    return res

print(maxIndexDiff([34, 8, 10, 3, 2, 80, 30, 33, 1], 9))





