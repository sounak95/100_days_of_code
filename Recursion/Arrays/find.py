

def find(arr, target, index):
    if index==len(arr):
        return  False
    return arr[index]==target or find(arr, target, index+1)

def find_index(arr, target, index):
    if index == len(arr):
        return -1
    if arr[index]==target:
        return index
    return find_index(arr, target, index+1)

def find_index_last(arr, target, index):
    if index==-1:
        return -1
    if arr[index]==target:
        return index

    return find_index_last(arr, target, index - 1)

l1=[]
def find_all_index(arr, target, index):
    if index==len(arr):
        return
    if arr[index]==target:
        l1.append(index)
    find_all_index(arr, target, index+1)

def find_all_index_1(arr, target, index, l1):
    if index==len(arr):
        return l1
    if arr[index]==target:
        l1.append(index)
    return find_all_index_1(arr, target, index+1, l1)

def find_all_index_2(arr, target, index):
    l1=[]
    if index==len(arr):
        return l1
    if arr[index]==target:
        l1.append(index)
    ans_from_below_calls = find_all_index_2(arr, target, index+1)
    l1.extend(ans_from_below_calls)
    return l1

if __name__ == "__main__":
    arr=[2, 3, 1, 4, 4, 5]
    # print(find(arr,9,0))
    # print(find_index(arr, 9, 0))
    # print(find_index_last(arr, 3, len(arr)-1))
    # find_all_index(arr, 4, 0)
    # print(l1)
    # l1=[]
    # print(find_all_index_1(arr, 4, 0,l1))
    print(find_all_index_2(arr, 4, 0))