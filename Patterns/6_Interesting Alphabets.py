'''
Code : Interesting Alphabets
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE
Input format :
N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 26
Sample Input 1:
8
Sample Output 1:
H
GH
FGH
EFGH
DEFGH
CDEFGH
BCDEFGH
ABCDEFGH
Sample Input 2:
7
Sample Output 2:
G
FG
EFG
DEFG
CDEFG
BCDEFG
ABCDEFG
'''

n= int(input())

start_char_1 = chr(ord('A')+n-1)

for i in range(1,n+1):
    start_char = chr(ord(start_char_1)-i)
    for j in range(1, i+1):
        print(chr(ord(start_char) +j)  , end='')
    print()