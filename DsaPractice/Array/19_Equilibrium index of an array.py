

def findEquilibrium(a,n):
    # Code here
    total_sum= sum(a)
    left_sum=0
    for  i,ele in enumerate(a):
        total_sum-=ele
        if left_sum==total_sum:
             return i
        left_sum+=ele
    return -1


