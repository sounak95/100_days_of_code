
# https://www.geeksforgeeks.org/remove-duplicates-from-a-given-string/



def remove_duplicates_sorted(s):
    ip_index=1
    res_index=1

    while(ip_index<len(s)):
        current_char = s[ip_index]
        prev_char = s[ip_index-1]
        if current_char!=prev_char:
            s[res_index] = current_char
            res_index+=1
        ip_index+=1

    return "".join(s[:res_index])



def removeDups(string):
    l1= list(string)
    l1.sort()
    print(l1)
    # print("".join(l1))
    return remove_duplicates_sorted(l1)


string = "geeksforgeeks"
print(removeDups(string))