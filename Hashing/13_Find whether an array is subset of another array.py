# https://www.geeksforgeeks.org/find-whether-an-array-is-subset-of-another-array-set-1/

# two pointer

def isSubset_1( a1, a2, n, m):
    a1.sort()
    a2.sort()
    i=0
    j=0
    while(i<n and j<m):
        if a1[i]<a2[j]:
            i+=1
        elif a1[i]==a2[j]:
            i+=1
            j+=1
        elif a1[i]>a2[j]:
            return "No"

        # print(j)
    if j==m:
        return "Yes"
    else:
        return "No"

def isSubset( a1, a2, n, m):
    hash=set()
    for ele in a1:
        hash.add(ele)

    for ele in a2:
        if ele in hash:
            continue
        else:
            return "No"
    return "Yes"


a1 = [11, 1, 13, 21, 3, 7]
a2 = [11, 3, 7, 1]

print(isSubset(a1,a2,len(a1), len(a2)))