
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/equilibrium-point-1587115620

# User function Template for python3
class Solution:
    # Complete this function

    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, A, N):
        sum = 0

        for ele in A:
            sum += ele

        left_sum = 0
        for i, ele in enumerate(A):
            sum -= ele
            if sum == left_sum:
                return i + 1

            left_sum += ele

        return -1


# Your code here