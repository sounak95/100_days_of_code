

def digit_sum(n):
    if n%10==n:
        return n
    else:
        return n%10 + digit_sum(n//10)


if __name__ == "__main__":
    n=32146
    print(digit_sum(n))