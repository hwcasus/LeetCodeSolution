# Binary Tree Preorder Traversal
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        value = []
        if not root:
            return []
        
        value += [root.val]
        if root.left:
            value += self.preorderTraversal(root.left)
        if root.right:
            value += self.preorderTraversal(root.right)
        return value
        
    def preorderTraversalIteratively(self, root):
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