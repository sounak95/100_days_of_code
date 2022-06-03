"""

Repeated Character Whose First Appearance is Leftmost
Given a string, find the repeated character present first in the string.

Examples:

Input  : geeksforgeeks
Output : g
(mind that it will be g, not e.)

Input  : abcdabcd
Output : a

Input  : abcd
Output : -1
No character repeats
Asked in: Goldman Sachs internship


How to solve this problem using one traversal of input string?

Method 1 (Traversing from Left to Right) We traverse the string from left to right. We keep track of the leftmost index of every character. If a character repeats, we compare its leftmsot index with current result and update the result if result is greater

static int NO_OF_CHARS = 256;

    /* The function returns index of the first
    repeating character in a string. If
    all characters are repeating then
    returns -1 */
    static int firstRepeating(char[] str)
    {
        // Initialize leftmost index of every
        // character as -1.
        int[] firstIndex = new int[NO_OF_CHARS];
        for (int i = 0; i < NO_OF_CHARS; i++)
        {
            firstIndex[i] = -1;
        }

        // Traverse from left and update result
        // if we see a repeating character whose
        // first index is smaller than current
        // result.
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < str.length; i++)
        {
            if (firstIndex[str[i]] == -1)
            {
                firstIndex[str[i]] = i;
            }
            else
            {
                res = Math.min(res, firstIndex[str[i]]);
            }
        }

        return (res == Integer.MAX_VALUE) ? -1 : res;
    }

"""

# Python 3 program to find first repeating
# character
NO_OF_CHARS = 256
def firstRepeating(str):
    firstIndex=[-1]*NO_OF_CHARS
    res= float('inf')
    for i, ch in enumerate(str):
        if firstIndex[ord(ch)]==-1:
            firstIndex[ord(ch)]=i
        else:
            res=min(res, firstIndex[ord(ch)])
    return res

# Driver function
if __name__ == '__main__':
    str = "geeksforgeeks"
    index = firstRepeating(str)
    if (index == -1):
        print("Either all characters are distinct or string is empty")
    else:
        print("First Repeating character is",str[index])