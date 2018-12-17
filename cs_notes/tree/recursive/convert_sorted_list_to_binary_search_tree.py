# 109. Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        def construct(vals):
            if not vals: return None
            idx = len(vals)//2
            root = TreeNode(vals[idx])
            root.left = construct(vals[:idx])
            root.right = construct(vals[idx+1:])
            return root

        return construct(vals)
