


def largestNumber(arr):

    n= len(arr)
    for i in range(n):
        arr[i] = str(arr[i])

    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+arr[j]<arr[j]+arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return str(int("".join(arr)))





if __name__ == "__main__":
    a = [54, 546, 548, 60]
    print(largestNumber(a))