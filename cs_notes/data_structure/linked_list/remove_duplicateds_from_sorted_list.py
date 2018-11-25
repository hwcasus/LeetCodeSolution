# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        rest = current = head

        while rest:
            if rest.val != current.val:
                current.next = rest
                current = current.next    
            rest = rest.next
            
        current.next = None
        return head
