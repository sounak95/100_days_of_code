
# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next

            while curr !=groupNext:
                next = curr.next
                curr.next=prev
                prev=curr
                curr=next

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev= tmp

        return dummy.next


    def getKthNode(self, curr, k):
        while curr and k>0:
            curr= curr.next
            k-=1
        return curr

