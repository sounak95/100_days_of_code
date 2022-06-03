"""

Calculate sum of all numbers present in a string
Given a string containing alphanumeric characters, calculate sum of all numbers present in the string.

Examples:

Input:  1abc23
Output: 24

Input:  geeks4geeks
Output: 4

Input:  1abc2x30yz67
Output: 100

Input:  123abc
Output: 123

"""

str="123abc1"
sum=0
temp=''

for ch in str:
    if ch.isdigit():
        temp+=ch
    else:
        sum+=int(temp)
        temp='0'
sum+=int(temp)
print(sum)