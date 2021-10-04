# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        queue = [root]
        p_val, q_val = p.val, q.val
        large_val, small_val = (p_val, q_val) if p_val > q_val else (q_val, p_val)

        while queue:
            curr = queue.pop(0)
            if small_val <= curr.val <= large_val:
                return curr

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)