# Binary Tree Inorder  Traversal
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        value = []
        if not root:
            return []
        
        if root.left:
            value += self.inorderTraversal(root.left)
        value += [root.val]
        if root.right:
            value += self.inorderTraversal(root.right)
        return value
        
    def inorderTraversalIteratively(self, root):
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
            if type(curr) == int:
                visited.append(curr)
                continue
            elif curr:
                queue.append(curr.right)
                queue.append(curr.val)
                queue.append(curr.left)
        
        return visited