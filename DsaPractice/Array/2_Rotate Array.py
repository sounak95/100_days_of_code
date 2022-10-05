

#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self,A,D,N):
        #Your code here
        if D>N:
            D=D-N
        temp=[]
        for i in range(D):
            temp.append(A[i])
        k=0
        for i in range(D,N):
            A[k]= A[i]
            k+=1
        k=0
        for i in range(N-D,N):
            A[i] = temp[k]
            k+=1



