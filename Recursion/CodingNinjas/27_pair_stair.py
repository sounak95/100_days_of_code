'''
Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
Input format :
String S
Output format :
Modified string
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
hello
Sample Output 1:
hel*lo
Sample Input 2 :
aaaa
Sample Output 2 :
a*a*a*a
'''



def pair_stair(string):
    # Please add your code here
    if len(string)==1 or len(string)==0:
        return string
    if string[0]==string[1]:
        return string[0] + "*" + pair_stair(string[1:])
    else:
        return string[0] + pair_stair(string[1:])

# Main
string = input().strip()
print(pair_stair(string))