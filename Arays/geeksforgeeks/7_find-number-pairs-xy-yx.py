

# https://www.geeksforgeeks.org/find-number-pairs-xy-yx/

def countPairsBruteForce(X, Y):

    count=0
    for ele_x in X:
        for ele_y in Y:
            if pow(ele_x,ele_y)> pow(ele_y, ele_x):
                count+=1
    return count

print(countPairsBruteForce([2, 1, 6], [1, 5]))
