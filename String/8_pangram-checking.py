"""
Pangram Checking
Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.

Examples : The quick brown fox jumps over the lazy dog ” is a Pangram [Contains all the characters from ‘a’ to ‘z’]
“The quick brown fox jumps over the dog” is not a Pangram [Doesn’t contains all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing]

We create a mark[] array of Boolean type. We iterate through all the characters of our string and whenever we see a character we mark it. Lowercase and Uppercase are considered the same. So ‘A’ and ‘a’ are marked in index 0 and similarly ‘Z’ and ‘z’ are marked in index 25.

"""
str1="The quick brown fox jumps over the lazy do"
flag=True
mark= [False]*26

str1=str1.lower()

for ch in str1:
    if ord('a')<=ord(ch)<=ord('z'):
        mark[ord(ch)-ord('a')]=True

for i,item in enumerate(mark):
    if item==False:
        flag=False
        print(f"Missing char {chr(i+ ord('a'))}")
        print(f"{str1} is not a panagram")
        break

if flag:
    print(f"{str1} is a panagram")