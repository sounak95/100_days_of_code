
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/maximize-number-of-1s0905


def findZeroes(arr, n, m) :
    # code here
    l=0
    l1=[]
    count=0
    max_len =0
    for r in range(n):
        l1.append(arr[r])
        if arr[r]==0:
            count+=1
        while(count>m):
            if arr[l]==0:
                count-=1
            l1.remove(arr[l])
            l+=1
        max_len = max(max_len,len(l1) )
    return max_len