
def firstDuplicateValueBruteForce(array):
    # Write your code here.
    min_index=len(array)
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]==array[j]:
                min_index=min(min_index,j)
    if min_index==len(array):
        return -1
    return array[min_index]

def firstDuplicateValue(array):
    # Write your code here.
    seen=set()
    for ele in array:
        if ele in seen:
            return ele
        else:
            seen.add(ele)
    return -1


print(firstDuplicateValue([2, 1, 5, 2, 3, 3, 4]))
