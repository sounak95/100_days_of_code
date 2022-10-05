
# https://practice.geeksforgeeks.org/problems/implement-strstr/1

def strstr(s,x):
    #code here
    # index=-1
    for i in range(len(s)-len(x)+1):
        flag=True
        index=i
        for j in range(len(x)):
            if s[i+j]!=x[j]:
                flag=False
                break
        if flag:
            return index
    return -1

print(strstr("GeeksForGeeks", "Fr"))

