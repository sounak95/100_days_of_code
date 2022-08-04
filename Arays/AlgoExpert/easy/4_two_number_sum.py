# two pointer

def twoNumberSum(array, targetSum):
    array.sort()
    left=0
    right=len(array)-1
    while(left<right):
        currentSum=array[left]+array[right]
        if currentSum==targetSum:
            return [array[left], array[right]]
        if currentSum<targetSum:
            left+=1
        if currentSum>targetSum:
            right-=1
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))