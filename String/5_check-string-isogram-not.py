"""
Check if a string is Isogram or not
Given a word or phrase, check if it is isogram or not. An Isogram is a word in which no letter occurs more than once.

Examples:

Input : Machine
Output : True
"Machine" does not have any character repeating,
it is an Isogram

Input : Geek
Output : False
"Geek" has 'e' as repeating character,
it is not an Isogram
"""

# Approach1
def is_isogram1(str):
    str=str.lower()
    letter_list=[]
    for ch in str:
        if ch in letter_list:
            return False
        else:
            letter_list.append(ch)
    return True

# Approach2
def is_isogram2(str):
    str=str.lower()
    count=[0]*26
    for ch in str:
        count[ord(ch)-ord('a')]+=1
        if count[ord(ch)-ord('a')]>1:
            return False
    return True

if __name__ == '__main__':
    print(is_isogram1("Machine"))
    print(is_isogram1("isogram"))
    print(is_isogram1("GeeksforGeeks"))
    print(is_isogram1("Alphabet "))

    print("***************************")
    print(is_isogram2("Machine"))
    print(is_isogram2("isogram"))
    print(is_isogram2("GeeksforGeeks"))
    print(is_isogram2("Alphabet "))