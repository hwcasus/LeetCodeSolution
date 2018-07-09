"""
Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:

    Input: 1->2
    Output: false

Example 2:

    Input: 1->2->2->1
    Output: true

Follow up:
    Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True
        
        p = head
        d = {}
        l = 0
        while p:
            if p.val not in d:
                d[p.val] = 0
            d[p.val] += 1
            p = p.next
            l += 1
        
        for k, v in d.items():
            if v%2 != 0:
                if l%2 != 0:
                    p = head
                    for i in range(int((l-1)/2)):
                        p = p.next
                    if k != p.val:
                        return False
                else: 
                    return False

        return True