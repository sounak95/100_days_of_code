'''
Maximum Profit on App
Send Feedback
You have made a smartphone app and want to set its subscription price such that the profit earned is maximised. There are certain users who will subscribe to your app only if their budget is greater than or equal to your price.
You will be provided with a list of size N having budgets of subscribers and you need to return the maximum profit that you can earn.
Lets say you decide that price of your app is Rs. x and there are N number of subscribers. So maximum profit you can earn is :
 m * x
where m is total number of subscribers whose budget is greater than or equal to x.
Input format :
Line 1 : N (No. of subscribers)
Line 2 : Budget of subscribers (separated by space)
Output Format :
 Maximum profit
Constraints :
1 <= N <= 10^6
1 <=budget[i]<=9999
Sample Input 1 :
4
30 20 53 14
Sample Output 1 :
60
Sample Output 1 Explanation :
Price of your app should be Rs. 20 or Rs. 30. For both prices, you can get the profit Rs. 60.
Sample Input 2 :
5
34 78 90 15 67
Sample Output 2 :
201
Sample Output 2 Explanation :
Price of your app should be Rs. 67. You can get the profit Rs. 201 (i.e. 3 * 67).
'''

# 14 20 30 53
def maximumProfit(arr):
    max_profit = float('-inf')
    arr.sort()
    n=len(arr)
    for i in range(n):
        count=n-i
        sum=count*arr[i]
        print(sum)
        if sum>max_profit:
            max_profit=sum
    return max_profit



#brute force
def maximumProfit1(arr):
	#Implement Your Function here
    max_profit=float('-inf')
    for i in range(len(arr)):
        sum=arr[i]
        for j in range(len(arr)):
            if i!=j:
                if arr[i]<=arr[j]:
                    sum+=arr[i]
        # print(sum)
        if sum>max_profit:
            max_profit=sum
    return max_profit

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)