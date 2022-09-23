'''
Code : Triangle of Numbers
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4



The dots represent spaces.



Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1:
5
Sample Output 1:
           1
         232
       34543
     4567654
   567898765
Sample Input 2:
4
Sample Output 2:
           1
         232
       34543
     4567654
'''

n= int(input())

for i in range(1,n+1):
    for j in range(1, n-i+1):
        print('.', end='')
    p=i
    for j in range(1, i+1):
        print(p, end='')
        p+=1
    p-=1
    for j in range(p-1, i-1, -1):
        print(j, end='')
    print()