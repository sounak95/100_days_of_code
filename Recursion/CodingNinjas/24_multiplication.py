'''
Multiplication (Recursive)
Send Feedback
Given two integers M & N, calculate and return their multiplication using recursion. You can only use subtraction and addition for your calculation. No other operators are allowed.
Input format :
Line 1 : Integer M
Line 2 : Integer N
Output format :
M x N
Constraints :
0 <= M <= 1000
0 <= N <= 1000
Sample Input 1 :
3
5
Sample Output 1 :
15
Sample Input 2 :
4
0
Sample Output 2 :


'''

def mul(n1,n2):
    if n2==0 or n1==0:
        return 0
    return n1 + mul(n1,n2-1)

print(mul(int(input()),int(input())))