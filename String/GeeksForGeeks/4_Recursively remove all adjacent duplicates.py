
# https://practice.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates0744/1

def rremove(s):
    temp=""
    while(temp!=s):
        temp=s
        s=remove(s)

        print(temp)
        print(s)
        print("********")
    return temp


def remove(s):
    i=0
    n=len(s)
    res=""
    while(i<n):
        if i<n-1 and s[i]==s[i+1]:
            while(i<n-1 and s[i]==s[i+1]):
                i+=1
        else:
            res+=s[i]
        i+=1

    return res


def remove1(s):
    i=0
    n=len(s)
    res=""
    while(i<n):
        if i<n-1 and s[i]==s[i+1]:
            while(i<n-1 and s[i]==s[i+1]):
                i+=1
        else:
            res+=s[i]
            i+=1

    return res

print(rremove("azxxzy"))
print(remove1("azxxzzzzyyyy"))