
# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

# User function Template for python3

class Solution:

    def issafe(self, row, col, m, n, visited):
        if row ==-1 or row ==n or col==-1 or col==n or visited[row][col] or m[row][col]==0:
            return False
        return True

    def print_path_util(self, row, col, m, n, path, possiblepaths, visited):
        if row ==-1 or row ==n or col==-1 or col==n or visited[row][col] or m[row][col]==0:
            return

        if row ==n-1 and col==n-1:
            possiblepaths.append(path)
            return

        visited[row][col] = True

        if self.issafe(row+1, col, m, n, visited):
            path+='D'
            self.print_path_util(row+1, col, m,n, path, possiblepaths, visited)
            # backtracking
            path = path[:-1]

        if self.issafe(row, col-1, m, n, visited):
            path+='L'
            self.print_path_util(row, col-1, m,n, path, possiblepaths, visited)
            # backtracking
            path = path[:-1]

        if self.issafe(row-1, col, m, n, visited):
            path+='U'
            self.print_path_util(row-1, col, m,n, path, possiblepaths, visited)
            # backtracking
            path = path[:-1]

        if self.issafe(row, col+1, m, n, visited):
            path+='R'
            self.print_path_util(row, col+1, m,n, path, possiblepaths, visited)
            # backtracking
            path = path[:-1]

        # backtracking
        visited[row][col] = False


    def findPath(self, m, n):
        possible_paths =[]
        path =""
        visited = [[False for _ in range(n)] for _ in range(n)]

        self.print_path_util(0,0,m,n,path, possible_paths, visited)
        return possible_paths







# code here


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