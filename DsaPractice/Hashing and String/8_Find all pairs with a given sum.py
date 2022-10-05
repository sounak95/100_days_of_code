
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-hashing/problem/find-all-pairs-whose-sum-is-x5808

class Solution:
    def allPairs(self, A, B, X):
        # Your code goes here

        map = set()
        l1 = []
        for i, ele in enumerate(B):
            map.add(ele)

        for i, ele in enumerate(A):
            goal = X - ele
            if goal in map:
                l1.append((ele, goal))
        return l1

s=Solution()
print(s.allPairs([-1, -2, 4, -6, 5, 7], [6, 3, 4, 0],8 ))


