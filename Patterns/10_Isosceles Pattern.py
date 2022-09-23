'''
...1
..121
.12321
1234321
'''

n= int(input())

for i in range(1,n+1):
    for j in range(1, n-i+1):
        print('.', end='')
    for j in range(1,i+1):
        print(j, end='')
    k=i-1
    for j in range(k,0,-1):
        print(j, end='')
    print()