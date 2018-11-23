# Binary Tree Postorder Traversal
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        val = []
        if root.left:
            val += self.postorderTraversal(root.left)
        if root.right:
            val += self.postorderTraversal(root.right)
        
        val.append(root.val)
        
        return val
    def postorderTraversalIteratively(self, root):
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
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        return list(reversed(visited)) # or visited[::-1]