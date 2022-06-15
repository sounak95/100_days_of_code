
# https://leetcode.com/problems/move-zeroes/

def move_zeros(nums):
    j=0
    for num in nums:
        if num!=0:
            nums[j]=num
            j+=1
    for i in range(j, len(nums)):
        nums[i]=0
    return nums

print(move_zeros([0,1,0,3,12]))