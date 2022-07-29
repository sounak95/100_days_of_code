
# https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1


class Solution:

    def isPalin(self, word):

        start = 0
        end = len(word) - 1

        while (start < end):
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        return True

    def longestPalin(self, S):
        # code here
        n = len(S)
        max_len = 0
        longest_substr = ""
        for i in range(n):
            for j in range(i, n):
                substr = S[i:j + 1]
                if self.isPalin(substr):
                    if len(substr) > max_len:
                        longest_substr = substr
                        max_len = len(substr)
        return longest_substr



s="cbbd"

S=Solution()
print(S.longestPalin(s))
