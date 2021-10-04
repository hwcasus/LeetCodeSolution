# https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.result = [1]
        def helper(root):
            # get distance and value
            if not root:
                return 0, -1001

            left_dist, left_val = helper(root.left)
            right_dist, right_val = helper(root.right)

            left_dist = 0 if root.val != left_val else left_dist
            right_dist = 0 if root.val != right_val else right_dist

            self.result.append(left_dist + right_dist + 1)
            return 1 + max(left_dist, right_dist), root.val

        helper(root)
        return max(self.result) - 1