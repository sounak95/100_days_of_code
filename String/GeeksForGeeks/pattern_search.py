txt = input("Enter Text:\n")
pat = input("Enter Pattern:\n")

pos = txt.find(pat)
print(pos)
while pos >= 0:
    print(pos)
    pos = txt.find(pat, pos + 1)