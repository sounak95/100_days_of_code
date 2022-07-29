

# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

def removeDuplicates( s):
    stack =[]

    for ch in s:
        if  len(stack)!=0 and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)

print(removeDuplicates("azxxzy"))
