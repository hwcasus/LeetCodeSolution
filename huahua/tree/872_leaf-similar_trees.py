# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def helper(sub_root, tmp=None):
            if not sub_root:
                return tmp

            if tmp is None:
                tmp = []

            if sub_root.left:
                tmp = helper(sub_root.left, tmp)
            if sub_root.right:
                tmp = helper(sub_root.right, tmp)

            if not sub_root.left and not sub_root.right:
                tmp.append(sub_root.val)
            return tmp

        return helper(root1) == helper(root2)