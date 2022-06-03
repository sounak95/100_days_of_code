"""

Given a binary string, count number of substrings that start and end with 1.
Given a binary string, count number of substrings that start and end with 1. For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.

Source: Amazon Interview Experience | Set 162
A Simple Solution is to run two loops. Outer loops picks every 1 as starting point and inner loop searches for ending 1 and increments count whenever it finds 1.

Input:
00100101

Output:
3
"""


str=input()
n=len(str)
count=0
for i in range(n):
    if str[i]=='1':
        for j in range(i+1,n):
            if str[j]=='1':
                count+=1
print(count)