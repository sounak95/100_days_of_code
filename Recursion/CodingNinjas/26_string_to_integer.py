

def str_to_int(str,n):
    if n<0:
        return 0
    return int(str[0])*pow(10,n)+ str_to_int(str[1:],n-1)


str1=input()
print(str_to_int(str1,len(str1)-1))
