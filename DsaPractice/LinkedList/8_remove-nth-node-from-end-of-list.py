

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        # code here
        dummyNode = ListNode(0)
        dummyNode.next = head

        left = dummyNode
        right = head

        while (n > 0):
            right = right.next
            n -= 1

        while (right):
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummyNode.next
