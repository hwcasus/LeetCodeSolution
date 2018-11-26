# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            tmp = []
            for curr in queue:
                print ('q', *queue)
                if not curr.left and not curr.right: return depth
                if curr.left: tmp.append(curr.left)
                if curr.right: tmp.append(curr.right)
                print ('t', *tmp) 
            queue = tmp
            
    def minDepthSlow(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            num_layer = len(queue)
            for i in range(num_layer):
                curr = queue.pop(0)
                if not curr.left and not curr.right:return depth
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
    
    def minDepthRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        l, r = self.minDepth(root.left), self.minDepth(root.right)
        
        # This line means 
        # if (min(l, r) == 0): l if l or r
        return (min(l, r) or (l or r)) + 1 