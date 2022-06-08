
def count(n):
    return helper(n,0)

def helper(n, c):
    if n==0:
        return c
    rem = n % 10
    n=n//10
    if rem==0:
        return helper(n,c+1)
    else:
        return helper(n,c)

if __name__ == "__main__":
    print(count(302100040))
    print(count(0))