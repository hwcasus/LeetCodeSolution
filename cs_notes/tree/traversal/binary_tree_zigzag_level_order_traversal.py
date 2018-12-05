# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root: return []

        stack = [root]
        # 使用 stack 才可以達到反過來的效果 ; queue 會在第三層開始亂掉
        rets = []
        while stack:
            ret = []
            new_stack = []
            for i in range(len(stack)):
                curr = stack.pop()
                ret.append(curr.val)
                if len(rets)%2 == 1:
                    if curr.right: new_stack.append(curr.right)
                    if curr.left: new_stack.append(curr.left)
                else:
                    if curr.left: new_stack.append(curr.left)
                    if curr.right: new_stack.append(curr.right)
            stack = new_stack
            rets.append(ret)
        return rets


