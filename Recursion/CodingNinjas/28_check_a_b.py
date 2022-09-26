'''

Check AB
Send Feedback
Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'
If all the rules are followed by the given string, return true otherwise return false.
Input format :
String S
Output format :
'true' or 'false'
Constraints :
1 <= |S| <= 1000
where |S| represents length of string S.
Sample Input 1 :
abb
Sample Output 1 :
true
Sample Input 2 :
abababa
Sample Output 2 :
false
Explanation for Sample Input 2
In the above example, a is not followed by either "a" or "bb", instead it's followed by "b" which results in false to be returned.

'''
def check_a_b(str,i):
    if i==len(str):
        return True
    if i==0:
        # The string begins with an 'a'
        if str[i]!='a':
            return False
    # Each 'a' is followed by nothing or an 'a' or "bb"
    if str[i]=='a' and i!=len(str)-1:
        if  (str[i+1]!='a' and str[i+1:i+3]!='bb'):
            return False
    # Each "bb" is followed by nothing or an 'a'
    if str[i:i+2]=='bb' and i+2!=len(str):
        if str[i+2]!='a':
            return False
    return check_a_b(str,i+1)

if(check_a_b(input(),0)):
    print("true")
else:
    print("false")