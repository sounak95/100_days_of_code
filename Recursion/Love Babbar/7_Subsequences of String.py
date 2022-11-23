
# https://www.codingninjas.com/codestudio/problems/subsequences-of-string_985087?leftPanelTab=0&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_16

from os import *
from sys import *
from collections import *
from math import *

def helper(str, i, output, ans):
    if i>=len(str):
        if len(output)!=0:
            l1=output.copy()
            ans.append("".join(l1))
        return

    helper(str,i+1,output, ans)

    output.append(str[i])
    helper(str, i + 1, output, ans)
    output.pop()

def subsequences(str):

    # Write your code here
    i=0
    output=[]
    ans=[]
    helper(str,i,output,ans)
    return ans

print(subsequences("abc"))