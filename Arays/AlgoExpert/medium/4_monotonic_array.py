
def breakDirection(direction, currentElement, prevElement):
    diff=currentElement-prevElement
    if direction>0:
        return diff<0
    return diff>0

def isMonotonic(array):
    # Write your code here.
    if len(array)<=2:
        return True
    direction=array[1]-array[0]
    for i in range(2,len(array)):
        if direction==0:
            print("abc")
            direction=array[i]-array[i-1]
            continue
        if breakDirection(direction, array[i], array[i-1]):
            return False
    return True

print(isMonotonic( [-1, -5, -10, -1100, -1100, -1101, -1101, -9001]))

