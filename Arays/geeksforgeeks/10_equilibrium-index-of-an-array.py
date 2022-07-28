

# https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

def equilibrium(arr):
    total_sum=sum(arr)
    left_sum=0

    for i, num in enumerate(arr):

        total_sum-=num
        if total_sum==left_sum:
            return i

        left_sum +=num



# Driver code
arr = [-7, 1, 5, 2, -4, 3, 0]
print ('First equilibrium index is ',
       equilibrium(arr))