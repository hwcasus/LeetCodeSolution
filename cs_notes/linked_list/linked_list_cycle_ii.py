# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head: ListNode) -> ListNode:
        # Revisit 20210730
        if head is None or head.next is None:
            return None

        slow = head.next
        fast = head.next.next

        while slow != fast:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        此題需要透過數學證明
        但結論來說就是從 head 到環入口的距離 == 從 slow, fast 交錯點到環入口的距離
        """
        if not head: return None
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return slow


        return None



