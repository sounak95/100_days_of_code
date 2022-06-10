

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

print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6],0))
