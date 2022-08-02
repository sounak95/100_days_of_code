# https://www.geeksforgeeks.org/sort-elements-by-frequency/

#code

def sortByFrequency(arr, n):
    f={}
    for ele in arr:
        f[ele] = f.get(ele,0) +1

    print(f)

    arr.sort(key=lambda x:(-f[x], x))
    print(arr)




# Driver program
arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
n = len(arr)

sortByFrequency(arr, n)

# print(arr)