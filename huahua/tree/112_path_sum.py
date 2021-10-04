# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(sub_root, target):
            if not sub_root:
                return False

            if (
                sub_root.left is None
                and sub_root.right is None
                and sub_root.val == target
            ):
                return True

            return (
                helper(sub_root.left, target - sub_root.val)
                or helper(sub_root.right, target - sub_root.val)
            )

        return helper(root, targetSum)