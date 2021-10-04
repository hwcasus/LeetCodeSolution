# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        carry = []
        result = []

        def helper(root):
            if not root:
                return False

            carry.append(root.val)
            left = helper(root.left)
            right = helper(root.right)

            if not left and not right and sum(carry) == targetSum:
                result.append(carry.copy())

            carry.pop()
            return True

        helper(root)
        return result