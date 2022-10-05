

# https://practice.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1

class Solution:

    # dorted
    def removeDuplicates(self, str):
        str=list(str)
        str.sort()
        ip_index =1
        res_index=1
        while(ip_index<len(str)):
            current_char = str[ip_index]
            prev_char = str[ip_index-1]
            if(current_char!=prev_char):
                str[res_index] = current_char
                res_index+=1
            ip_index+=1
        return  "".join(str[:res_index])


s=Solution()
print(s.removeDuplicates("geeksforgeeks"))
# code here