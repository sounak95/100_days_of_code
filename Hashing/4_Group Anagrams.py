# https://leetcode.com/problems/group-anagrams/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m={}
        for str in strs:
            sorted_string = "".join(sorted(str))
            if sorted_string in m:
                m[sorted_string].append(str)
            else:
                m[sorted_string]=[str]
        return list(m.values())

s=Solution()
strs=["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))