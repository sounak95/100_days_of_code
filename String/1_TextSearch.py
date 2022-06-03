'''

Input:
BlUeBe1Bl*fjal9jkl
Bl
Output:
Pattern Bl found at 0
Pattern Bl found at 7


'''
text=input()
n=len(text)
pat=input()
m=len(pat)

for i in range(n-m+1):
    flag=True
    for j in range(m):
        if text[i+j]!=pat[j]:
            flag=False
            break
    if flag:
        print(f"Pattern {pat} found at {i}")

