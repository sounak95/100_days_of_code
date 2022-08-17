
# https://www.lintcode.com/problem/659/


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        str1=""
        for word in strs:
            str1+=str(len(word))+'#' + word
        return str1

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        i=0
        res=[]
        while(i<len(str)):
            j=i
            while(str[j]!='#'):
                j+=1
            length= int(str[i:j])
            word = str[j+1:j+1+length]
            res.append(word)
            i=j+1+length
        return res


input=["lint","code","love","you"]
s=Solution()
print(s.encode(input))
print(s.decode(s.encode(input)))