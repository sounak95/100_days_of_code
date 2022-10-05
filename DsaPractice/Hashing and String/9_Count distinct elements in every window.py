
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-hashing/problem/count-distinct-elements-in-every-window


class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        map={}
        count=0
        res=[]
        for i in range(K):
            if A[i] not in map:
                count+=1
            map[A[i]] = map.get(A[i],0)+1
        res.append(count)

        for i in range(K,N):
            if map[A[i-K]]==1:
                count-=1

            map[A[i-K]]-=1

            if A[i] not in map or map[A[i]]==0:
                count+=1

            map[A[i]] = map.get(A[i],0)+1
            res.append(count)
            # print(map)
            # print(count)

        return res

s=Solution()
print(s.countDistinct([1,2,1,3,4,2,3], 7,4))

