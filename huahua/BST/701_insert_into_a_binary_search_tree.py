# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def helper(root):
            if root.val < val:
                if root.right:
                    helper(root.right)
                else:
                    root.right = TreeNode(val)
            else:
                if root.left:
                    helper(root.left)
                else:
                    root.left = TreeNode(val)

        helper(root)
        return root