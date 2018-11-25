# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/description/

tion for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def get_mid(head):
            slow = fast = head
            while fast.next:
                slow = slow.next
                fast = fast.next
                if fast.next:
                    fast = fast.next
            return slow
        
        def compare_two_list(head_a, head_b):
            while head_a and head_b:
                if head_b.val != head_a.val:
                    return False
                head_b = head_b.next
                head_a = head_a.next
            return True
        
        def reverse_list(head):
            new_head = None
            while head:
                current = head
                head = head.next
                current.next = new_head
                new_head = current
            return new_head
        
        if not head or not head.next:
            return True

        return compare_two_list(
            head,
            reverse_list(get_mid(head))
        )
        
    def isPalindromeList(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True
        
        l = []
        p = head
        while p:
            l+=[p.val]
            p = p.next
        
        return l[::-1]==l
