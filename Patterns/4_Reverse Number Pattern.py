'''
Code : Reverse Number Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
21
321
4321
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
1
21
321
4321
54321
'''

n= int(input())

for i in range(1, n+1):
    p=i
    for j in range(1, i+1):
        print(p, end='')
        p-=1
    print()