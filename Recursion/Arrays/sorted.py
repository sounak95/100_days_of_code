
def sorted(arr, index):
    if index==len(arr)-1:
        return True
    return arr[index]<arr[index+1] and sorted(arr, index+1)



if __name__ == "__main__":
    arr=[1, 2, 3, 5, 16,2]
    print(sorted(arr,0))