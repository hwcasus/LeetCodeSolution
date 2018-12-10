# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        prev = None
        def go(root):
            if root:
                go(root.right)
                go(root.left)
                
                nonlocal prev
                root.right = prev
                root.left = None
                prev = root
        
        go(root)
        
    def flattenA(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        用前序全部裝到list中
        然後將後面的Node當成前面Node的右邊孩子
        """
        ret = []
        def go(root):
            if root:
                ret.append(root)
                go(root.left)
                go(root.right)
            
        go(root)
        for i in range(len(ret)-1):
            ret[i].left = None
            ret[i].right = ret[i+1]
        
