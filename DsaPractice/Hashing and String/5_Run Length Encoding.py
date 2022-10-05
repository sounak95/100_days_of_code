
# https://practice.geeksforgeeks.org/problems/run-length-encoding/1

def encode(arr):
    # Code here
    ip_index=1
    output=[]
    current_running_length=1
    curr_char = arr[0]
    while(ip_index<len(arr)):
        curr_char = arr[ip_index]
        prev_char = arr[ip_index-1]

        if curr_char!=prev_char:
            output.append(prev_char)
            output.append(str(current_running_length))
            current_running_length=1
        else:
            current_running_length+=1
        ip_index+=1
    if curr_char:
        output.append(curr_char)
        output.append(str(current_running_length))
        # current_running_length += 1

    return "".join(output)
print(encode("c"))
