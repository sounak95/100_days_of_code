
# 0 1 1 2 3 5
def fibo(n):
    if n==1 or n==2:
        return 1
    fib_n_1=fibo(n-1)
    fib_n_2 = fibo(n-2)
    output= fib_n_1+fib_n_2
    return output




if __name__ == "__main__":
    print(fibo(4))