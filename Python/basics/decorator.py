
def f1(func):
    def wrapper(*args, **kwargs):
        print("started")
        val = func(*args, **kwargs)
        print("Ended")
        return val
    return wrapper

@f1
def add(a,b):
    return a+b

print(add(5,10))