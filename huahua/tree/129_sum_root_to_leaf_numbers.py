# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = []

        def helper(root, carry=0):
            if not root.left and not root.right:
                self.result.append(carry*10 + root.val)
            else:
                if root.left:
                    helper(root.left, carry * 10 + root.val)
                if root.right:
                    helper(root.right, carry * 10 + root.val)


        helper(root)
        return sum(self.result)