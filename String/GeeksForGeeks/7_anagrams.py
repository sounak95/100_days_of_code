# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/


class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        COUNT_CHAR=[0] * 256

        for ch in a:
            COUNT_CHAR[ord(ch)]+=1

        for ch in b:
            COUNT_CHAR[ord(ch)]-=1

        for i in range(256):
            if COUNT_CHAR[i]!=0:
                return False

        return True

s=Solution()
a = "allergy"
b = "allergic"
print(s.isAnagram(a,b))
