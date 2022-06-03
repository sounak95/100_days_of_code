"""
Check whether two strings are anagram of each other
Write a function to check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are anagram of each other.

Anagram Words

Listen - Silent

Triangle - Integral

Method 1 (Use Sorting)

Sort both strings
Compare the sorted strings

Time Complexity: O(nLogn)

Method 2 (Count characters)
This method assumes that the set of possible characters in both strings is small. In the following implementation, it is assumed that the characters are stored using 8 bit and there can be 256 possible characters.

Create count arrays of size 256 for both strings. Initialize all values in count arrays as 0.
Iterate through every character of both strings and increment the count of character in the corresponding count arrays.
Compare count arrays. If both count arrays are same, then return true.

Input:
listen
silent
Output:
True
"""

str1=input()
n1=len(str1)
str2=input()
n2=len(str2)

if n1!=n2:
    print("False")
else:
    flag=True
    NO_OF_CHARS=256
    count = [0] * NO_OF_CHARS

    for i in range(n1):
        count[ord(str1[i])]+=1

    for i in range(n1):
        count[ord(str2[i])] -= 1

    for i in range(NO_OF_CHARS):
        if count[i]!=0:
            # print(chr(i))
            # print(count[i])
            flag = False
            break
    print(flag)