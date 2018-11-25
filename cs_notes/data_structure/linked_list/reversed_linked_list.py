# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        new_head = None
        
        while head:
            current = head
            head = head.next
            current.next = new_head
            new_head = current
        
        return new_head
