

def permutations(p,up):
    if len(up)==0:
        print(p)
        return

    ch = up[0]
    for i in range(0,len(p)+1):
        f=p[0:i]
        s=p[i:len(p)]
        permutations(f+ch+s, up[1:])

def permutationsList(p,up):
    if len(up)==0:
        l1=[]
        l1.append(p)
        return l1

    ch = up[0]
    ans=[]
    for i in range(0,len(p)+1):
        f=p[0:i]
        s=p[i:len(p)]
        ans.extend(permutationsList(f+ch+s, up[1:]))

    return ans

def permutationsCount(p,up):
    if len(up)==0:
        return 1

    ch = up[0]
    count=0
    for i in range(0,len(p)+1):
        f=p[0:i]
        s=p[i:len(p)]
        count+=permutationsCount(f+ch+s, up[1:])

    return count


if __name__ == "__main__":
    permutations("", "abc")
    print(permutationsList("", "abc"))
    print(permutationsCount("", "abc"))