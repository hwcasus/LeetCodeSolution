# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        ret = head.next
        super_head = ListNode(0, head)

        while head and head.next:
            # s -> 2
            second = head.next

            # 1 -> 3
            head.next = head.next.next

            # 2 -> 1
            second.next = head

            # 0 -> 2
            super_head.next = second

            # 0 == 1
            super_head = second.next

            # h == 3
            head = super_head.next


        return ret

    def show(self, head):
        s = []
        while head:
            s.append(head.val)
            head = head.next

        print(s)