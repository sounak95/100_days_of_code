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

    # print(longest_substr)
    return max_length

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring(""))


