
def countCharFreq(string):
    charFreq={}

    for ch in string:
        if ch in charFreq:
            charFreq[ch]+=1
        else:
            charFreq[ch]=1

    return charFreq


def updateMaxFreq(charFreq, maxCharFreq):
    for ch in charFreq:
        if ch in maxCharFreq:
            maxCharFreq[ch]= max(charFreq[ch], maxCharFreq[ch])
        else:
            maxCharFreq[ch]=charFreq[ch]

def convertDictToList(dict):
    l1=[]
    for ch in dict:
        freq= dict[ch]

        for _ in range(freq):
            l1.append(ch)

    return l1


def minimumCharactersForWords(words):
    # Write your code here.
    maxCharFreq={}

    for word in words:
        charFreq=countCharFreq(word)
        updateMaxFreq(charFreq, maxCharFreq)

    return convertDictToList(maxCharFreq)


print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))