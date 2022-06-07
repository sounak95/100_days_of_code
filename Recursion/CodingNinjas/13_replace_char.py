
def replaceChar(s,a,b):
    if len(s)==0:
        return ""
    smallOutput=replaceChar(s[1:],a,b)
    if s[0]==a:
        return b+ smallOutput
    else:
        return s[0]+smallOutput

def replaceChar1(s,a,b):
    if len(s)==0:
        return ""
    if s[0]==a:
        return b+ replaceChar1(s[1:],a,b)
    else:
        return s[0]+replaceChar1(s[1:],a,b)



print(replaceChar("cc",'c','x'))
print(replaceChar1("cc",'c','x'))