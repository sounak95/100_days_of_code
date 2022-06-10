
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    currentDiff=float('inf')
    smallestDiff=float('inf')

    smallestPair=[]

    idx1=0
    idx2=0

    while(idx1<len(arrayOne) and idx2<len(arrayTwo)):
        firstNum=arrayOne[idx1]
        secondNum=arrayTwo[idx2]

        if firstNum<secondNum:
            currentDiff=secondNum-firstNum
            idx1+=1
        elif secondNum<firstNum:
            currentDiff=firstNum-secondNum
            idx2+=1
        else:
            return [firstNum,secondNum]
        if currentDiff<smallestDiff:
            smallestDiff=currentDiff
            smallestPair=[firstNum,secondNum]
    return smallestPair


print(smallestDifference([-1, 5, 10, 20, 28, 3],[26, 134, 135, 15, 17]))
