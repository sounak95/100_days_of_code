

# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/maximize-number-of-1s0905

def findZeroes(arr, n, m) :
    # code here
    l=0
    l1 =[]
    res = float('-inf')
    count=0
    for r in range(n):
        # print(l1)
        if arr[r]==0:
            count+=1
        l1.append(arr[r])

        while(count>m):
            if arr[l]==0:
                count-=1
            # print(l)
            # print(l1)
            l1.remove(arr[l])
            l += 1

        res = max(res, len(l1))
    return res

print(findZeroes([1,0,1,0], 4,0))
