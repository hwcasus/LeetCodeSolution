# https://leetcode.com/problems/distribute-coins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        self.moves = 0

        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            required = (root.val - 1) + left + right
            self.moves += abs(required)
            return required

        helper(root)
        return self.moves