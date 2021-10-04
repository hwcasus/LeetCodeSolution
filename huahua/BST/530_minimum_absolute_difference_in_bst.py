# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        self.diff = float('inf')
        self.prev = float('-inf')

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            self.diff = min(self.diff, (root.val - self.prev))
            self.prev = root.val
            inorder(root.right)

        inorder(root)
        return self.diff