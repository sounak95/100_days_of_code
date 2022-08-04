# hashing

NO_OF_CHAR=256
def firstNonRepeatingCharacter(string):
    # Write your code here.
    count = [0] * NO_OF_CHAR
    for ch in string:
        count[ord(ch)]+=1
    for i,ch in enumerate(string):
        if count[ord(ch)]==1:
            return i
    return -1

print(firstNonRepeatingCharacter("abcdcaf"))