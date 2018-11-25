# 725. Split Linked List in Parts
# https://leetcode.com/problems/split-linked-list-in-parts/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
            return [[]]*k
        
        n = 1
        current = root
        while current.next:
            n = n + 1
            current = current.next
        
        q, r = n//k, n%k
        counts = enumerate(1 + q if i < r else q for i in range(k))
        result = [None]*k    
        for i, c in counts:
            if not c: continue

            result[i] = root
            for _ in range(c-1): root = root.next
            root.next, root = None, root.next
            
        return result
