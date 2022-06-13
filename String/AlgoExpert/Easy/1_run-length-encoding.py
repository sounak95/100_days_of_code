

def runLengthEncoding(string):
    # Write your code here.
    encodedStringCharacters=[]
    currentrunningLength=1

    for i in range(1, len(string)):
        currentChar=string[i]
        previousChar=string[i-1]

        if currentChar!=previousChar or currentrunningLength==9:
            encodedStringCharacters.append(str(currentrunningLength))
            encodedStringCharacters.append(previousChar)
            currentrunningLength=1
        else:
            currentrunningLength+=1

    encodedStringCharacters.append(str(currentrunningLength))
    encodedStringCharacters.append(string[-1])
    return "".join(encodedStringCharacters)


print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
