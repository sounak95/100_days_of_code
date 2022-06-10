

def threeNumberSum_brute_force(array, targetSum):
    # Write your code here.
    l1=[]
    for i, num1 in enumerate(array):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                if array[i]+array[j]+array[k]==targetSum:
                    l2=[array[i], array[j], array[k]]
                    l1.append(sorted(l2))
    return l1

def threeNumberSum(array, targetSum):
    # Write your code here.
    l1=[]
    array.sort()
    for i, num in enumerate(array):
        left=i+1
        right=len(array)-1
        while(left<right):
            currentSum= num+array[left]+array[right]
            if currentSum==targetSum:
                l1.append([num, array[left], array[right]])
                left+=1
                right-=1
            elif currentSum<targetSum:
                left+=1
            elif currentSum>targetSum:
                right-=1
    return l1




print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6],0))
