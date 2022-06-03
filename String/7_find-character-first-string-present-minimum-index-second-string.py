"""

Find the character in first string that is present at minimum index in second string
Given a string str and another string patt. Find the character in patt that is present at the minimum index in str. If no character of patt is present in str then print ‘No character present’.

Examples:

Input: str = “geeksforgeeks”, patt = “set”
Output: e
Both e and s of patt are present in str,
but e is present at minimum index, which is 1.

Input: str = “adcffaet”, patt = “onkl”
Output: No character present

"""

# Python3 implementation to find the character in
# first that is present at minimum index
# in second String

def printMinIndexChar(str,patt):
    min_index= float('inf')
    for ch_pat in patt:
        for i,ch_st in enumerate(str):
            if ch_pat==ch_st and i<min_index:
                min_index=i
    if min_index==float('inf'):
        print("No character present")
    else:
        print("Minimum index character is {}".format(str[min_index]))



# Driver code
Str = "geeksforgeeks"
patt = "set"
printMinIndexChar(Str, patt)