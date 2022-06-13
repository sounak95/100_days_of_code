
def getNewLetter(letter, key):
    key=key%26
    newLettercode=ord(letter)+key
    return chr(newLettercode) if newLettercode<=122 else chr(96+newLettercode%122)

def getNewLetter1(letter, key):
    key=key%26
    alphabet="abcdefghijklmnopqrstuvwxyz"
    newLettercode=alphabet.index(letter)+key
    return alphabet[newLettercode%26]

def caesarCipherEncryptor(string, key):
    # Write your code here.
    str1=''
    for ch in string:
        str1 += getNewLetter1(ch,key)
    return str1

print(caesarCipherEncryptor("xyz",2))