

# https://www.geeksforgeeks.org/find-uncommon-characters-two-strings/

class Solution:
    def UncommonChars(self, A, B):
        # code here
        MAX = 26

        map1 = [0] * MAX
        map2 = [0] * MAX
        for ch in A:
            ch_idx = ord(ch) - ord('a')
            map1[ch_idx] = 1

        for ch in B:
            ch_idx = ord(ch) - ord('a')
            map2[ch_idx] = 1

        str1 = ""
        for i in range(0, MAX):
            ch = chr(i + ord('a'))
            if map1[i] != map2[i]:
                str1 += ch

        if str1 != "":
            return str1
        return -1

s=Solution()
A = "geeksforgeeks"
B = "geeksquiz"
print(s.UncommonChars(A,B))