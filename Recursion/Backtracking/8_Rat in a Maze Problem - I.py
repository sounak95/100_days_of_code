
# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1


# User function Template for python3
import copy
class Solution:

    def findPathHelper(self, i, j, a, n, ans, move, vis):
        if i == n-1 and j == n-1:
            ans.append(move)
            return

        # downward
        if (i + 1 < n and vis[i + 1][j] == 0 and a[i + 1][j] == 1):
            vis[i][j] = 1
            self.findPathHelper(i + 1, j, a, n, ans, move + "D", vis)
            vis[i][j] = 0

        # left
        if (j-1 >=0 and vis[i][j - 1] == 0 and a[i][j-1] == 1):
            vis[i][j] = 1
            self.findPathHelper(i, j - 1, a, n, ans, move + "L", vis)
            vis[i][j] = 0

        # right
        if (j+1 < n and vis[i][j + 1] == 0 and a[i][j + 1] == 1):
            vis[i][j] = 1
            self.findPathHelper(i, j + 1, a, n, ans, move + "R", vis)
            vis[i][j] = 0

        # up
        if (i-1 >=0 and vis[i-1][j] == 0 and a[i - 1][j] == 1):
            vis[i][j] = 1
            self.findPathHelper(i - 1, j, a, n, ans, move + "U", vis)
            vis[i][j] = 0

    def findPath(self, m, n):
        # code here
        # rows, cols = (n, n)
        # vis = [[0] * cols] * rows

        vis = []
        s = [0] * n
        for i in range(n):
            vis.append(copy.deepcopy(s))

        ans = []
        if m[0][0] == 1:
            self.findPathHelper(0, 0, m, n, ans, "", vis)
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        matrix = [[0 for i in range(n[0])] for j in range(n[0])]
        k = 0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k += 1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            for x in result:
                print(x, end=" ")
            print()
# } Driver Code Ends