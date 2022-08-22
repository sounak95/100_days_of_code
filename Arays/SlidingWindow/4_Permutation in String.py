

# https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        s1Count=[0]*26
        s2Count=[0]*26

        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')]+= 1
            s2Count[ord(s2[i])- ord('a')] += 1

        matches=0
        for i in range(26):
            if s1Count[i]==s2Count[i]:
                matches+=1
        l=0
        for r in range(len(s1), len(s2)):
            # print(matches)

            if matches==26:
                return True

            index = ord(s2[r])-ord('a')
            s2Count[index]+=1
            if  s2Count[index] ==  s1Count[index]:
                matches+=1
            elif s2Count[index] == s1Count[index]+1:
                matches-=1

            index =ord(s2[l])- ord('a')
            s2Count[index]-=1
            if  s2Count[index] ==  s1Count[index]:
                matches+=1
            elif s2Count[index] == s1Count[index]-1:
                matches-=1

            l+=1
        #
        # print(matches)
        # print(s1Count)
        # print(s2Count)
        # print(s2[l:r])

        return matches==26

s=Solution()
s1 = "abc"
s2 = "bbbca"
print(s.checkInclusion(s1,s2))



