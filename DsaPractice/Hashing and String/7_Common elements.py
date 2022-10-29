
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-hashing/problem/common-elements1132

# User function Template for python3

class Solution:
    def commonElements(self, A, B, C, n1, n2, n3):
        # your code here
        A.sort()
        B.sort()
        C.sort()
        i = 0
        j = 0
        k = 0
        l1 = []
        while (i < n1 and j < n2 and k < n3):
            if A[i] == B[j] == C[k]:
                if A[i] not in l1:
                    l1.append(A[i])
                i += 1
                j += 1
                k += 1
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1
        return l1


# {
# Driver Code Starts
# Initial Template for Python 3


t = int(input())
for tc in range(t):
    n1, n2, n3 = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    ob = Solution()

    res = ob.commonElements(A, B, C, n1, n2, n3)

    if len(res) == 0:
        print(-1)
    else:
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends
