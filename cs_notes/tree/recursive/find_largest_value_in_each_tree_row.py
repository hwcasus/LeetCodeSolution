# 515. Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        queue = [root]
        ret = []
        while queue:
            val = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                val.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            # print(val)
            ret.append(max(val))
        
        return ret
