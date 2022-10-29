


def dice(p,target):
    if target==0:
        print(p)
        return
    i=1
    while(i<=6 and i<=target):
        dice(p+str(i), target-i)
        i+=1

def diceRet(p,target):
    if target==0:
        l1=[]
        l1.append(p)
        return l1
    i=1
    l1=[]
    while(i<=6 and i<=target):
        l1.extend(diceRet(p+str(i), target-i))
        i+=1
    return l1

def diceFace(p,target, face):
    if target==0:
        print(p)
        return
    i=1
    while(i<=face and i<=target):
        diceFace(p+str(i), target-i, face)
        i+=1

def diceFaceRet(p,target, face):
    if target==0:
        l1=[]
        l1.append(p)
        return l1
    i=1
    l1=[]
    while(i<=face and i<=target):
        l1.extend(diceFaceRet(p+str(i), target-i, face))
        i+=1
    return l1






if __name__ == "__main__":
    dice("", 4)
    print(diceRet("",4))
    diceFace("", 4, 6)
    print(diceFaceRet("", 4, 6))