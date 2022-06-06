



def subseqRet(p, up):
    if len(up)==0:
        l1=[]
        l1.append(p)
        return l1

    ch=up[0]

    list_left =[]
    list_right=[]
    list_left= subseqRet(p+ch, up[1:])
    list_right = subseqRet(p,up[1:])

    list_left.extend(list_right)
    return list_left

def subseqAscii(p, up):
    if len(up)==0:
        print(p)
        return

    ch=up[0]

    subseqAscii(p+ch, up[1:])
    subseqAscii(p,up[1:])
    subseqAscii(p+ str(ord(ch)), up[1:])


def subseqAsciiRet(p, up):
    if len(up)==0:
        l1=[]
        l1.append(p)
        return l1

    ch=up[0]

    list_1 =[]
    list_2=[]
    list_3 = []
    list_1= subseqAsciiRet(p+ch, up[1:])
    list_2 = subseqAsciiRet(p,up[1:])
    list_3  = subseqAsciiRet(p +str( ord(ch)), up[1:])

    list_1.extend(list_2)
    list_1.extend(list_3)
    return list_1


if __name__ == "__main__":
    # print(subseqRet("","abc"))
    print(subseqAsciiRet("","abc"))
    subseqAscii("","abc")