# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        ptr_a, ptr_b = headA, headB
        
        while(ptr_a!=ptr_b):
            ptr_a = headB if ptr_a is None else ptr_a.next
            ptr_b = headA if ptr_b is None else ptr_b.next
        
        return ptr_a
