
# https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/

def largestNumber(arr):

    n= len(arr)
    for i in range(n):
        arr[i] = str(arr[i])
    print(list(reversed(sorted(arr)))) # incorrect approach
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]+arr[j]<arr[j]+arr[i]:
                # print(f"swapping {arr[i]} and {arr[j]}")
                arr[i], arr[j] = arr[j], arr[i]

        # print(arr)

    # print(arr)
    return str(int("".join(arr)))





if __name__ == "__main__":
    a = [54, 546, 548, 60]
    a = [3,30,34,5,9]
    print(largestNumber(a))