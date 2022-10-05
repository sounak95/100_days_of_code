
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-arrays/problem/stock-buy-and-sell2615

def stockBuySell(price, n):
    # code here
    l=0
    intervals=[]
    i,j =l,0
    max_profit = float('-inf')
    for r in range(1,n):
        if price[l]<price[r]:
            profit = price[r] - price[l]
            if profit>max_profit:
                max_profit=profit
                i,j = l, r
            else:
                l = r
                max_profit = float('-inf')
                if i != j:

                    print("(" + str(i) +" "+  str(j)+")", end=' ')
                    i=j=0
        else:
            l=r
            max_profit = float('-inf')
            if i!=j:
                print("(" + str(i) +" "+  str(j)+")", end=' ')
                i = j = 0
    if i != j:
        print("(" + str(i) +" "+  str(j)+")", end=' ')


price=[100, 180, 260, 310, 40, 535, 695]
n=7
price=[23, 13, 25, 29, 33, 19, 34, 45, 65, 67]
n=10
price=[886,2777,6915,7793,8335,5386,492,6649,1421,2362,27,8690,59]
stockBuySell(price,n)

