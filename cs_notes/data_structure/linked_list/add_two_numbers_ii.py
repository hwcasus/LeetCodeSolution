# 445. Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbersSlow(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        
        if not l1:
            return l2
        if not l2:
            return l1
        
        def l_to_s(l):
            s = []
            while l:
                s.insert(0, l)
                l = l.next
            return s
        
        l1_stack, l2_stack = l_to_s(l1), l_to_s(l2)
        current = None
        new_val = 0
        
        while l1_stack or l2_stack:
            
            if l1_stack:
                l1_top = l1_stack.pop(0)
                new_val += l1_top.val
            if l2_stack:
                l2_top = l2_stack.pop(0)
                new_val += l2_top.val
            
            
            head = ListNode(new_val%10)
            head.next = current
            current = head
            new_val//=10
            
        if new_val != 0:
            head = ListNode(new_val)
            head.next = current
            
        return head
                
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        v1, v2 = 0, 0
        
        while l1 or l2:
            if l1:
                v1 = v1 *10 + l1.val
                l1 = l1.next
            if l2:
                v2 = v2 *10 + l2.val
                l2 = l2.next
        
        v = str(v1+v2)
        
        fake_head = current = ListNode(None)
        for c in v:
            current.next = ListNode(int(c))
            current = current.next
           
        return fake_head.next
