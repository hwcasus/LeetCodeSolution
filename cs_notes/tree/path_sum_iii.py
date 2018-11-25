# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.pathSumAct(root, 0, sum, {0:1})
        return self.result
        
    def pathSumAct(self, root, so_far, sum, cache):
        """
        cache to record all the so_far value
        while we travel down the tree,
        we check if so_far + root.val was the missing
        """
        if root:
            and_now = so_far + root.val
            self.result += cache.get(and_now - sum, 0)
            cache.setdefault(and_now, 0)
            
            print (and_now, and_now - sum, self.result)
            
            cache[and_now] += 1
            self.pathSumAct(root.left, and_now, sum, cache)
            self.pathSumAct(root.right, and_now, sum, cache)
            cache[and_now] -= 1
    
    def pathSumSlow(self, root, sum):
        if not root: return 0
        ret = self.pathSumSlowRoot(root, sum) + self.pathSumSlow(root.right, sum) + self.pathSumSlow(root.left, sum)
        return ret

    def pathSumSlowRoot(self, root, sum):
        if not root: return 0
        ret = 0
        if root.val == sum :
            ret += 1
        sum -= root.val
        return ret + self.pathSumSlowRoot(root.left, sum) + self.pathSumSlowRoot(root.right, sum)
