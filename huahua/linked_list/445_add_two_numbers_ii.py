# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        v1 = "0"
        while l1:
            v1 += str(l1.val)
            l1 = l1.next


        v2 = "0"
        while l2:
            v2 += str(l2.val)
            l2 = l2.next

        v = int(v1) + int(v2)
        if v == 0:
            return ListNode(0)

        ret = None
        while v > 0:
            v, c = divmod(v, 10)
            ret = ListNode(c, ret)

        return ret