# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
    
        odd_head, even_head = head, head.next
        odd_ptr, even_ptr = odd_head, even_head
        
        # if total is odd, then even_ptr would be none
        # if total is even, then even_ptr.next would be none
        while even_ptr and even_ptr.next:
            odd_ptr.next = even_ptr.next
            odd_ptr = odd_ptr.next
            even_ptr.next = odd_ptr.next
            even_ptr = even_ptr.next

        odd_ptr.next = even_head
        
        return odd_head
