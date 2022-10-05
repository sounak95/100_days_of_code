
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/array-of-alternate-ve-and-ve-nos1401

class Solution:
    def rearrange_1(self,arr, n):
        # code here
        positive_list=[]
        negative_list =[]

        for ele in arr:
            if ele>=0:
                positive_list.append(ele)
            else:
                negative_list.append(ele)
        pos_k=0
        neg_k=0
        print(positive_list)
        print(negative_list)
        for i in range(n):
            if i%2==0:
                if pos_k<len(positive_list):
                    arr[i] = positive_list[pos_k]
                    pos_k+=1
                else:
                    arr[i] = negative_list[neg_k]
                    neg_k += 1
            else:
                if neg_k<len(negative_list):
                    arr[i] = negative_list[neg_k]
                    neg_k+=1
                else:
                    arr[i] = positive_list[pos_k]
                    pos_k += 1

    def rearrange(self,arr, n):
        # code here
        positive_list=[]
        negative_list =[]

        for ele in arr:
            if ele>=0:
                positive_list.append(ele)
            else:
                negative_list.append(ele)

        i=0
        j=0
        k=0

        while(i< len(positive_list) and j< len(negative_list)):
            if k%2==0:
                arr[k] = positive_list[i]
                k+=1
                i+=1
            else:
                arr[k] = negative_list[j]
                k += 1
                j += 1

        while(i<len(positive_list)):
            arr[k]=positive_list[i]
            i+=1
            k+=1

        while(j<len(negative_list)):
            arr[k] = negative_list[j]
            j+=1
            k+=1

s=Solution()
s.rearrange([-5,-2,5,2,4,7,1,8,0,-8], 10)