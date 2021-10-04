# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pace = []

        if root:
            def helper(sub_root):
                if sub_root.left:
                    helper(sub_root.left)
                if sub_root.right:
                    helper(sub_root.right)

                pace.append(sub_root.val)

            helper(root)

        return pace