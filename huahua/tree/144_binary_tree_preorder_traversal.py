# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pace = []
        if root:
            def helper(sub_root):
                pace.append(sub_root.val)
                if sub_root.left:
                    helper(sub_root.left)
                if sub_root.right:
                    helper(sub_root.right)

            helper(root)

        return pace

    def preorderTraversal_bfs(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = [root]
        visited = []

        while queue:
            curr = queue.pop()
            visited.append(curr.val)
            if curr.right:
                queue.append(curr.right)
            if curr.left:
                queue.append(curr.left)

        return visited
