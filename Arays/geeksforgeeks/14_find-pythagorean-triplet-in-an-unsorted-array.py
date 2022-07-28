# https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/


def isTriplet(ar, ar_size):
    n=ar_size
    for i in range(ar_size):
        ar[i]= ar[i]*ar[i]

    ar.sort()

    for i in range(n-1, -1, -1):
        j=0
        k=i-1

        while(j<k):
            sum=ar[j]+ar[k]
            if sum==ar[i]:
                return True
            elif sum<ar[i]:
                j+=1
            else:
                k-=1
    return False





# Driver program to test above function */
ar = [3, 1, 4, 6, 5]
ar_size = len(ar)
if(isTriplet(ar, ar_size)):
    print("Yes")
else:
    print("No")