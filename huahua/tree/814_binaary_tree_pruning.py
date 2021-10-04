# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if not(root.left or root.right or root.val == 1):
            return None

        return root

    def pruneTree_v1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(sub_root):
            if not sub_root:
                return False

            if not (left_contain_one := helper(sub_root.left)):
                sub_root.left = None

            if not (right_contain_one := helper(sub_root.right)):
                sub_root.right = None

            return (
                left_contain_one
                or right_contain_one
                or sub_root.val == 1
            )

        if not helper(root):
            return None

        return root