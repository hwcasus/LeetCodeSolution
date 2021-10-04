# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ret = head = ListNode()

        while l1 and l2:
            if l1.val > l2.val:
                head.next = head = l2
                l2 = l2.next
            else:
                head.next = head = l1
                l1 = l1.next

        head.next = l1 or l2
        return ret.next