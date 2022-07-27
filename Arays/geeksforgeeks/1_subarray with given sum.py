# https://www.geeksforgeeks.org/find-subarray-with-given-sum/

def subArraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    n= len(nums)
    curr_sum=nums[0]
    start=0
    for i in range(1,n):
        while (curr_sum > k and start<i-1):
            curr_sum-=nums[start]
            start+=1

        if curr_sum==k:
            print(f"found between {start} and {i-1}")
            return

        curr_sum+=nums[i]
        # print(curr_sum)x
    if curr_sum == k:
        print(f"found between {start} and {i - 1}")
        return

    print("No subarray found")


arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum = 38

subArraySum(arr,sum)
