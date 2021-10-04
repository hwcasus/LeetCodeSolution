# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def helper(sub_root):
            if not sub_root:
                return 0

            left_depth = helper(sub_root.left)
            right_depth = helper(sub_root.right)

            if abs(left_depth - right_depth) > 1:
                self.balanced = False

            return 1 + max(left_depth, right_depth)

        helper(root)
        return self.balanced