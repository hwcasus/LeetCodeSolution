# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = head = ListNode()
        current_sum = 0

        while l1 or l2 or current_sum != 0:
            if l1:
                current_sum += l1.val
                l1 = l1.next
            if l2:
                current_sum += l2.val
                l2 = l2.next

            current_sum, digits = divmod(current_sum, 10)
            head.next = head = ListNode(digits)

        return ret.next


    def addTwoNumbersMe(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rest = 0

        ret = head = ListNode()

        while l1 and l2:
            digits = l1.val + l2.val + rest

            rest = digits // 10
            curr = digits % 10

            head.next = head = ListNode(curr)

            l1 = l1.next
            l2 = l2.next

        remain_node = l1 or l2
        while remain_node:
            digits = remain_node.val + rest

            rest = digits // 10
            curr = digits % 10

            head.next = head = ListNode(curr)
            remain_node = remain_node.next

        if rest:
            head.next = head = ListNode(rest)

        return ret.next