
# https://practice.geeksforgeeks.org/problems/count-the-triplets4615/1
# two pointer, three sum

class Solution:
    def countTriplet(self, arr, n):
        arr.sort()
        count=0
        for i in range(n-1,-1,-1):
            j=0
            k=i-1
            target=arr[i]
            while(j<k):
                sum=arr[j]+arr[k]
                if sum==target:
                    # print(f"found {target} with {arr[j] , arr[k]}")
                    j+=1
                    k-=1
                    count+=1
                elif sum<target:
                    j+=1
                else:
                    k-=1
        return count

s=Solution()
print(s.countTriplet([1, 5, 3, 2], 4))



