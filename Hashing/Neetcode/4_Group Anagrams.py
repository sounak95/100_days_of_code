# https://leetcode.com/problems/group-anagrams/

import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m=collections.defaultdict(list)
        for str in strs:
            count=[0] * 26
            for ch in str:
                count[ord(ch)-ord('a')] +=1
            m[tuple(count)].append(str)
        return m.values()

s=Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
