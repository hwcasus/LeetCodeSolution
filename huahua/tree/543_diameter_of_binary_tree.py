# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.result = []

        def helper(root):
            if not root:
                return 0

            left_diameter = helper(root.left)
            right_diameter = helper(root.right)

            self.result.append(left_diameter + right_diameter + 1)

            return 1 + max(left_diameter, right_diameter)

        helper(root)
        return max(self.result) - 1

