
# call by value applicable only for immutable objects like number, string

def change(x):
    x=x+2
x=100
change(x)
print(x)

def changeList(l2):
    l2.append("abc")

# call by reference, applicable for immutable objects
l1=["abc", "def"]
changeList(l1)
print(l1)