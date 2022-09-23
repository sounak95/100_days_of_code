'''
Code : Star Pattern
Send Feedback
Print the following pattern
Pattern for N = 4



The dots represent spaces.



Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1 :
3
Sample Output 1 :
   *
  ***
 *****
Sample Input 2 :
4
Sample Output 2 :
    *
   ***
  *****
 *******
'''

n= int(input())

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ', end='')
    for j in range(1, (2*i-1)+1):
        print('*', end='')
    print()