
# https://www.geeksforgeeks.org/reverse-words-in-a-given-string/

def reverse(word):
    word = list(word)
    start =0
    end=len(word)-1

    while(start<end):
        word[start], word[end] = word[end], word[start]
        start+=1
        end-=1

    return "".join(word)

def reverseWords(S):

    l1=[]
    for word in S.split(" "):
        l1.append(word)

    l1.reverse()
    return " ".join(l1)

S = "geeks quiz practice code"
S = "getting good at coding needs a lot of practice"
print(reverseWords(S))

