
# https://www.geeksforgeeks.org/write-your-own-atoi/

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        # Code here

        i=0
        isNegative=False
        if string[0]=='-':
            isNegative=True
            i+=1

        res=0

        while(i<len(string)):
            if not string[i].isdigit():
                return -1
            res = res*10 +   ord(string[i])-ord('0')
            i+=1
        if isNegative:
            return -1* res

        return res


s=Solution()
print(s.atoi("-123A"))

