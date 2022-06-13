def isPalindrome(string):
    # Write your code here.
    start=0
    end=len(string)-1

    while(start<end):
        if string[start]!=string[end]:
            return False
        start+=1
        end-=1
    return True

def longestPalindromicSubstring(string):
    # Write your code here.
    longest=""
    print(len(string))
    for i in range(len(string)):
        for j in range(i, len(string)):
            substr=string[i:j+1]
            print(f"i: {i} j: {j}")
            print(substr)
            if len(substr)>len(longest) and isPalindrome(substr):
                # print(substr)
                longest=substr
    return longest

print(longestPalindromicSubstring("it's highnoon"))


