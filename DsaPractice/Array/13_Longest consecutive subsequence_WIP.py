
class Solution:

    # arr[] : the input array
    # N : size of the array arr[]

    # Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self ,arr, N):
        res=float('-inf')
        for ele in arr:
            print(ele)
            count=0
            if ele-1 not in arr:
                count=1
                while(ele+count in arr):
                    count+=1
                    print(count)
            res= max(res, count)
        return res

# code here
s=Solution()
print(s.findLongestConseqSubseq([2,6,1,9,4,5,3],7))
