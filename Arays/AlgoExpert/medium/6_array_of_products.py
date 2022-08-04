# left array, right array

def arrayOfProducts(array):
    # Write your code here.
    leftProduct=[1 for _ in range(len(array))]
    rightProduct=[1 for _ in range(len(array))]
    prodcut=[1 for _ in range(len(array))]

    leftRunningProduct=1
    for i in range(len(array)):
        leftProduct[i]=leftRunningProduct
        leftRunningProduct*=array[i]

    rightRunningProduct=1
    for i in reversed(range(len(array))):
        rightProduct[i]=rightRunningProduct
        rightRunningProduct*=array[i]

    for i in range(len(array)):
        prodcut[i]=leftProduct[i]*rightProduct[i]
    print(leftProduct)
    print(rightProduct)
    return prodcut

print(arrayOfProducts([5, 1, 4, 2]))