

def sliding_window_brute_force(arr,k):
    MAX_SUM= float('-inf')

    for i in range(len(arr)-k+1):
        current_sum=0
        for j in range(k):
            current_sum+=arr[i+j]
        MAX_SUM = max(current_sum, MAX_SUM)
    return MAX_SUM

def sliding_window(arr,window_size):
    window_sum = sum([arr[i] for i in range(window_size)])
    MAX_SUM= window_sum

    for i in range(len(arr)-window_size):
        print(window_sum)
        window_sum= window_sum- arr[i]+ arr[i+window_size]
        MAX_SUM= max(window_sum, MAX_SUM)


    return MAX_SUM

print(sliding_window([1, 2, 100, -1, 5], 3))
# print(sliding_window_brute_force([1, 2, 100, -1, 5], 3))

