
MAX_NUM=256
def minimumCharactersForWords(words):
    # Write your code here.
    char_array = [False]*MAX_NUM
    l1=[]
    for word in words:
        for ch in word:
            if not char_array[ord(ch)]:
                char_array[ord(ch)]=True

    for word in words:
        for ch in word:
            if char_array[ord(ch)] and ch not in l1:
                l1.append(ch)

    return l1

print(minimumCharactersForWords(["this", "that", "did", "deed", "them!", "a"]))