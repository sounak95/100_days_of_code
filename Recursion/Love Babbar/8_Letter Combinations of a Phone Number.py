
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


class Solution(object):

    def solve(self, digits, output, index, ans, mapping):
        if index>= len(digits):
            l1 = output.copy()
            ans.append("".join(l1))
            return ans

        number= ord(digits[index]) -ord('0')
        values=mapping[number]

        for i, value in enumerate(values):
            output.append(value)
            self.solve(digits, output, index+1, ans, mapping)
            output.pop()

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans=[]
        if len(digits)==0:
            return ans
        output=[]
        index=0
        mapping=["", "", "abc", "def", "ghi", "jkl","mno","pqrs","tuv","wxyz"]
        self.solve(digits, output, index, ans, mapping)
        return ans

s=Solution()
print(s.letterCombinations("23"))

