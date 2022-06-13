
def countFrequency(character, target):
    freq=0
    for ch in target:
        if ch==character:
            freq+=1
    return freq

def generateDocument(characters, document):
    # Write your code here.
    alreadyCounted=set()
    for character in document:
        if character in alreadyCounted:
            continue
        else:
            alreadyCounted.add(character)
        characterFreq= countFrequency(character, characters)
        documentFreq = countFrequency(character,document)
        if documentFreq > characterFreq:
            return False

    return True

print(generateDocument("Bste!hetsi ogEAxpelrt x ","AlgoExpert is the Best!"))
print(generateDocument(" ","hello"))

