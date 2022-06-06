

def fact(n):
    if n==0:
        return 1
    small_output=n*fact(n-1)
    return small_output

if __name__ == "__main__":
    print(fact(5))