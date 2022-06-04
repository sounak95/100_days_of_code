

def sum(n):
    if n==1:
        return n
    return n+sum(n-1)



if __name__ == "__main__":
    print(sum(6))