

def nonConstructibleChange(coins):
    coins.sort()
    change_created=0
    for coin in coins:
        if coin>change_created+1:
            return change_created+1
        change_created+=coin
    return change_created+1

print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
print(nonConstructibleChange([ 1, 1,  3]))



