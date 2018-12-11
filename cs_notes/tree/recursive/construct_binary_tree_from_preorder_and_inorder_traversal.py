# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return None
        if len(preorder) == 1: return TreeNode(preorder[0])

        root_idx = inorder.index(preorder[0])
        in_left = inorder[:root_idx]
        in_right = inorder[root_idx+1:]
        pre_left = preorder[1:1+len(in_left)]
        pre_right = preorder[1+len(in_left):]

        root = TreeNode(inorder[root_idx])
        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)
        return root

