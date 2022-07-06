
def moveElementToEnd(array, toMove):
    # Write your code here.
    start=0
    end=len(array)-1

    while(start<end):
        while array[start]!=toMove and start<len(array)-1:
            start+=1
        while array[end]==toMove and end>0:
            end-=1

        if start<end:
            array[start], array[end]= array[end],array[start]
    return array

print(moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2],2))
print(moveElementToEnd([1, 2, 4, 5, 6],3))