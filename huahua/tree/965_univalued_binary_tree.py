# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        def helper(sub_root, root_val):
            if not sub_root:
                return True

            return (
                sub_root.val == root_val
                and helper(sub_root.left, root_val)
                and helper(sub_root.right, root_val)
            )

        return helper(root, root.val)


    def isUnivalTree_bfs(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = [root]
        value = root.val

        while queue:
            curr = queue.pop(0)
            if curr.val != value:
                return False

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return True