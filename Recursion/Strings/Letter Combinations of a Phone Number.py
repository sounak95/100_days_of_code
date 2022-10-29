
def pad(p,up):
    if len(up)==0:
        print(p)
        return
    digit = ord(up[0])-ord('0')
    for i in range((digit-1)*3,digit*3):
        ch = chr(ord('a') + i)
        pad(p+ch, up[1:])


def padRet(p,up):
    if len(up)==0:
        l1=[]
        l1.append(p)
        return l1
    digit = ord(up[0])-ord('0')
    l1=[]
    for i in range((digit-1)*3,digit*3):
        ch = chr(ord('a') + i)
        l1.extend(padRet(p+ch, up[1:]))

    return l1

def padCount(p,up):
    if len(up)==0:
        return 1
    digit = ord(up[0])-ord('0')
    count=0
    for i in range((digit-1)*3,digit*3):
        ch = chr(ord('a') + i)
        count+=padCount(p+ch, up[1:])

    return count

if __name__ == "__main__":
    pad("","12")
    print(padRet("","12"))
    print(padCount("", "12"))