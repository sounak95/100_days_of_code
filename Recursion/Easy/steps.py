
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

def numberOfSteps(n):
    return helper(n,0)

def helper(n,count):
    if n==0:
        return count
    elif n%2==0:
        return helper(n/2,count+1)
    else:
        return helper(n-1, count+1)


if __name__ == "__main__":
    print(numberOfSteps(123))