# https://www.geeksforgeeks.org/print-all-subarrays-with-0-sum/
# https://www.youtube.com/watch?v=C9-n_H7dsvU

# use hasing to store the occurances of prefix sum
class Solution:
    # Function to count subarrays with sum equal to 0.
    def findSubArrays(self, arr, n):
        map = {}

        prefix_sum = 0
        count = 0
        map[prefix_sum] = 1
        for i, ele in enumerate(arr):

            prefix_sum += ele

            if prefix_sum in map:
                # max_len = max(max_len, i-map[prefix_sum])
                # print(f"Subarray found from {map[prefix_sum]+1} to {i}")
                count += map[prefix_sum]

            map[prefix_sum] = map.get(prefix_sum, 0) + 1

        return count

        # return: count of sub-arrays having their sum equal to 0

