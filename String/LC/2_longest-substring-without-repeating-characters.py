# https://leetcode.com/problems/longest-substring-without-repeating-characters/


def lengthOfLongestSubstring_optimal(s):
    n= len(s)
    left=right=0
    m={}
    ans =0
    substr=""
    while(left<n and right<n):
        el=s[right]
        if el in m:
            left=max(left, m[el]+1)
        m[el]=right

        substr1 = s[left:right+1]
        len1 = right-left+1
        if len1>ans:
            ans=len1
            substr=substr1
        right += 1

        # ans= max(ans, right-left+1)
    return ans



# brute force
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    n= len(s)
    longest_substr=""
    max_length= 0
    for i in range(n):
        seen={}
        current_length=0
        for j in range(i,n):
            substr=s[i:j+1]
            if s[j] in seen:
                break
            seen[s[j]]=True
            current_length+=1
            if current_length>max_length:
                max_length=current_length
                longest_substr=substr

    print(longest_substr)
    return max_length

print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring(" "))
# print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring_optimal("abcabcbb"))
# print(lengthOfLongestSubstring_optimal(" "))
# print(lengthOfLongestSubstring_optimal(""))


