
# https://practice.geeksforgeeks.org/batch/MDP-1/track/mdcq-linkedlist/problem/check-if-linked-list-is-pallindrome


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def isPalindrome(self, head):
        #code here
        if not head:
            return
        temp=head
        st=[]
        while(temp):
            st.append(temp.data)
            temp=temp.next

        temp = head
        while(temp):
            stData = st.pop()
            if stData!=temp.data:
                return False
            temp=temp.next

        return True

