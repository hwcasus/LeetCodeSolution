# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            # For each node, return max if pick self and not pick self.
            if not root:
                return 0, 0

            left_pick_self, left_pick_child = helper(root.left)
            right_pick_self, right_pick_child = helper(root.right)

            pick_self = root.val + left_pick_child + right_pick_child
            pick_any_child = max(left_pick_self, left_pick_child) + max(right_pick_self, right_pick_child)

            return pick_self, pick_any_child

        return max(helper(root))