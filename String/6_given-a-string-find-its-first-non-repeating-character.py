"""
Given a string, find its first non-repeating character
Given a string, find the first non-repeating character in it. For example, if the input string is “GeeksforGeeks”, then output should be ‘f’ and if input string is “GeeksQuiz”, then output should be ‘G’.


We can use string characters as index and build a count array. Following is the algorithm.

1) Scan the string from left to right and construct the count array.
2) Again, scan the string from left to right and check for count of each
 character, if you find an element who's count is 1, return it.

"""

NO_OF_CHAR=256
def firstRepeating(str):
    count=[0]*NO_OF_CHAR
    for ch in str:
        count[ord(ch)]+=1
        if count[ord(ch)]>1:
            return ch
    return -1

def firstNonRepeating(str):
    count=[0]*NO_OF_CHAR
    for ch in str:
        count[ord(ch)]+=1
    for ch in str:
        if count[ord(ch)]==1:
            return ch
    return -1

# Driver program to test above function
string = "geeksforgeeks"
letter = firstRepeating(string)
print("First repeating character is " + letter)

letter = firstNonRepeating(string)
print("First non-repeating character is " + letter)