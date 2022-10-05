

# https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1


class Solution:

    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        st=[]
        for ch in x:
            if ch =="}":
                if not st or st[-1] !="{":
                    return False
                st.pop()
            elif ch =="]":
                if not st or st[-1] !="[":
                    return False
                st.pop()
            elif ch ==")":
                if not st or st[-1] !="(":
                    return False
                st.pop()
            else:
                st.append(ch)

        if not st:
            return True
        return False

s=Solution()
print(s.ispar("([]"))

# code here
