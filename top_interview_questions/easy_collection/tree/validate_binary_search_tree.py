"""
Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees. 

Example 1:

    Input:
        2
       / \
      1   3
    Output: true

Example 2:

        5
       / \
      1   4
         / \
        3   6
    Output: false
    Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
                is 5 but its right child's value is 4.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        return self.validate_bst(root, -sys.maxsize-1, sys.maxsize)
        
        
    def validate_bst(self, root, current_min, current_max):
        if not root:
            return True
        if (root.val >= current_max) or (root.val <= current_min): 
            return False
        return self.validate_bst(root.left, current_min, root.val) and self.validate_bst(root.right, root.val, current_max)