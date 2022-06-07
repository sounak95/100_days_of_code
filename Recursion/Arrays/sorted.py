
def sorted(arr, index):
    if index==len(arr)-1:
        return True
    if arr[index]>arr[index+1]:
        return False
    # return arr[index]<arr[index+1] and sorted(arr, index+1)
    return sorted(arr, index+1)



if __name__ == "__main__":
    arr=[1, 2, 3, 5, 26,16]
    print(sorted(arr,0))