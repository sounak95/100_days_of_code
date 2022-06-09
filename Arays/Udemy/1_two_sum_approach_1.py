


def findTwoSum(l1, targetToFind):
    for i in range(len(l1)):
        num_to_find= targetToFind-l1[i]
        for j in range(i+1,len(l1)):
            if l1[j]==num_to_find:
                return (i,j)
    return None

l1 = [1, 3, 7, 9, 2]
targetToFind = 11
print(findTwoSum(l1, targetToFind))
