
def sum(n):
    if n==0:
        return 0
    small_output=sum(n-1)
    output=n+small_output
    return output

if __name__ == "__main__":
    print(sum(5))