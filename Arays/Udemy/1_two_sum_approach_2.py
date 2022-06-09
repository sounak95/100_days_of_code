

def findTwoSum(nums, targetToFind):
    numsMap={}
    for i, ele in enumerate(nums):
        if ele in numsMap:
            currentMapVal=numsMap[ele]
            return currentMapVal, i
        else:
            numberToFind=targetToFind-ele
            numsMap[numberToFind]=i

        num_to_find= targetToFind-l1[i]

    return None

l1 = [1, 3, 7, 9, 2]
targetToFind = 11
print(findTwoSum(l1, targetToFind))
