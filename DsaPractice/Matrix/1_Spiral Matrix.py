#https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix):
        s_col=0
        n_cols = len(matrix[0])
        e_col=len(matrix[0])-1

        s_row=0
        n_rows =len(matrix)
        e_row=len(matrix)-1

        count=0
        l1=[]
        n_ele = (n_rows*n_cols)
        while count<n_ele:

            for i in range(s_col, e_col+1):
                l1.append(matrix[s_row][i])
                # print(matrix[s_row][i], end=' ')
                count+=1
            s_row += 1

            if count<n_ele:
                for i in range(s_row, e_row+1):
                    l1.append(matrix[i][e_col])
                    count+=1
                e_col -= 1

            if count < n_ele:
                for i in range(e_col, s_col-1,-1):
                    l1.append(matrix[e_row][i])
                    # print(matrix[e_row][i])
                    count+=1
                e_row-=1

            if count < n_ele:
                for i in range(e_row, s_row-1,-1):
                    l1.append(matrix[i][s_col])
                    count+=1
                s_col+=1

        return l1

s=Solution()
print(s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))