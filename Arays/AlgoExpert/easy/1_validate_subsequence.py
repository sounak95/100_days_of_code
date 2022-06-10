
def validate_subseuence(arr, seq):
    arr_idx=0
    seq_idx=0

    while(arr_idx<len(arr) and seq_idx<len(seq)):
        if arr[arr_idx]== seq[seq_idx]:
            seq_idx+=1
        arr_idx+=1
    return seq_idx==len(seq)

print(validate_subseuence([1,2,3,4,5,6], [2,4,6]))
print(validate_subseuence([1,2,3,4,5,6], [4,2,6]))
