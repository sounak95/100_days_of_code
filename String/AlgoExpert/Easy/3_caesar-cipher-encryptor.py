
def getNewLetter(letter, key):
    newLettercode=ord(letter)+key
    return chr(newLettercode) if newLettercode<=122 else chr(96+newLettercode%122)

def caesarCipherEncryptor(string, key):
    # Write your code here.
    str1=''
    for ch in string:
        str1 += getNewLetter(ch,key)
    return str1

print(caesarCipherEncryptor("xyz",2))