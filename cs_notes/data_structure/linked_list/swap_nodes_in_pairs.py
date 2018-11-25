# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        f_node, s_node = head, head.next
        done_end_node = None
        while f_node and s_node:
            
            f_node.next = s_node.next
            s_node.next = f_node
            
            if done_end_node:
                done_end_node.next = s_node
            else:
                head = s_node
            
            done_end_node = f_node
            f_node = f_node.next
            
            if f_node:
                s_node = f_node.next
            
        return head

    def swapPairsRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def swap(head):
            if head==None or head.next==None:
                return head
            
            temp=head.next
            head.next=swap(temp.next)
            temp.next=head
            head=temp
            return head

        
        return swap(head)
