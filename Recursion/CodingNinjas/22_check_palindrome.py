'''

Check Palindrome (recursive)
Send Feedback
Check whether a given String S is a palindrome using recursion. Return true or false.
Input Format :
String S
Output Format :
'true' or 'false'
Constraints :
0 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
racecar
Sample Output 1:
true
Sample Input 2 :
ninja
Sample Output 2:
false


'''

def rev(s,n):
    if n<0:
        return ""
    return s[n]+rev(s,n-1)

str1=input()
str2=rev(str1, len(str1.strip())-1)
if str2==str1:
    print("true")
else:
    print("false")

