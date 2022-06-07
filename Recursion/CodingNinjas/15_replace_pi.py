
def replacePi(s):
    if len(s)==1 or len(s)==0:
        return s
    if s.startswith("pi"):
        return "3.14" + replacePi(s[2:])
    else:
        return s[0]+ replacePi(s[1:])



print(replacePi("pippi"))