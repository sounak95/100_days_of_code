# https://www.youtube.com/watch?v=IUami0pKijo

# https://practice.geeksforgeeks.org/problems/array-pair-sum-divisibility-problem3257/1 : TODO

# https://practice.geeksforgeeks.org/problems/count-pairs-in-array-divisible-by-k/1

def codePair(nums, k):

    m={}
    res=0
    for num in nums:
        rem= num%k
        if rem!=0:
            res += m.get(k-rem, 0)
        else:
            res+=m.get(0,0)
        m[rem] = m.get(rem,0) +1
    # print(res)
    return res

arr = [5, 9, 36, 74, 52, 31, 42]
k = 3
print(codePair(arr,k))

