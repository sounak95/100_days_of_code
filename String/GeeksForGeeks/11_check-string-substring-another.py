
# https://practice.geeksforgeeks.org/problems/implement-strstr/1

def strstr(s,x):
    n=len(s)
    m=len(x)
    for i in range(n-m+1):
        flag=True
        for j in range(m):
            if s[i+j] !=x[j]:
                flag=False
                break
        if flag :
            return i

    return -1
# s= "ccdeecbdfedcbabfdfaebdaf"
#
# x= "fecfacbccfe"

s= "GeeksForGeeks"
x="For"

print(strstr(s,x))