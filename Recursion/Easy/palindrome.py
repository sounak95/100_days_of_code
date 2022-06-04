
import math


def rev(n, digits):
    if n%10==n:
        return n
    else:
        rem = n % 10
        n=n//10
        return rem * pow(10, digits-1) + rev(n,digits-1)

sum=0
def rev2(n):
    global sum
    if n==0:
        return 
    else:
        rem=n%10
        n=n//10
        sum=sum*10+rem
        rev2(n)


if __name__ == "__main__":
    n=121234
    digits= int(math.log10(n))+1
    print(rev(n,digits))
    # print(n==rev(n,digits))
    rev2(n)
    print(sum)