# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tmp = head
        vals = []
        while tmp:
            vals.append(tmp.val)
            tmp = tmp.next

        vals.sort()

        tmp = head
        for v in vals:
            tmp.val = v
            tmp = tmp.next

        return head

    def insertionSortListV1(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ret = tmp = ListNode(val=float('-inf'))

        while head:
            curr = head
            head = head.next

            # fine the node whose next should be curr
            while tmp.next and tmp.next.val < curr.val:
                tmp = tmp.next

            rest = tmp.next
            tmp.next = curr
            curr.next = rest
            tmp = ret

        return ret.next
