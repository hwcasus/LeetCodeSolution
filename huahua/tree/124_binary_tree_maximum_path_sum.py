# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.candidate = []

        def helper(root):
            if not root:
                return 0

            if not (root.left or root.right):
                self.candidate.append(root.val)
                return root.val

            left_val = max(0, helper(root.left))
            right_val = max(0, helper(root.right))


            self.candidate.append(root.val + left_val + right_val)
            return root.val + max(left_val, right_val)

        helper(root)
        return max(self.candidate)