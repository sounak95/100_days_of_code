
# https://leetcode.com/problems/reorder-list/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head

        while( fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second =slow.next
        slow.next, prev= None, None

        while(second):
            next = second.next
            second.next = prev
            prev = second
            second = next

        # merge two  halfs,

        first, second = head, prev

        while(second):
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2




