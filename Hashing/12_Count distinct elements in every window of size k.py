# https://www.geeksforgeeks.org/count-distinct-elements-in-every-window-of-size-k/
# https://practice.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1

class Solution:
    def countDistinct(self, A, N, K):
        map={}
        l1=[]
        count=0
        for i in range(K):
            if A[i] not in map:
                count+=1
            map[A[i]]= map.get(A[i],0) + 1


        l1.append(count)
        for i in range(K,N):
            if map[A[i-K]] ==1:
                count-=1
            map[A[i-K]]-=1

            if A[i] not in map or map[A[i]]==0:
                count+=1

            map[A[i]] = map.get(A[i],0)+1

            l1.append(count)
        return l1


s=Solution()
print(s.countDistinct([1, 2, 1, 3, 4, 2, 3], 7,4))