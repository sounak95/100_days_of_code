

# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists)==0:
            return None

        while(len(lists)>1):
            mergedLists=[]
            for i in range(0, len(lists), 2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                mergedLists.append(self.mergeTwoLists(l1,l2))
            lists=mergedLists

        return lists[0]

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail= dummy

        while(list1 and list2):
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next= list1

        if list2:
            tail.next = list2

        return dummy.next