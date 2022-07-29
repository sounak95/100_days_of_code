# https://www.geeksforgeeks.org/longest-common-prefix-using-sorting/#:~:text=The%20longest%20common%20prefix%20for,not%20share%20any%20starting%20characters.


class Solution:
    def longestCommonPrefix(self, arr):
        # code here

        n = len(arr)
        arr.sort()

        end=min(len(arr[0]), len(arr[n-1]))

        i=0
        while(i<end and arr[0][i]==arr[n-1][i]):
            i+=1

        if i!=0:
            return arr[0][:i]
        return -1


s=Solution()
# print(s.longestCommonPrefix(["geeksforgeeks", "geeks", "geek", "geezer"]))
# print(s.longestCommonPrefix(["apple", "ape", "april"]))
print(s.longestCommonPrefix(["hello", "world"]))


