
with open('test1.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()