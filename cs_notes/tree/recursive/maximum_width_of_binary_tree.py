# 662. Maximum Width of Binary Tree
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        本題想法如下
        馬上就想到要用 BFS
        一開始是把 None 也放在 queue 裡面, 想說計算裡面非None的頭尾的距離
        但後來想想, root 的左右孩子必定是在 2*root_idx, 2*root_idx+1
        所以不需要放 None, 只要順便把 idx 跟 Node 一起放在queue就好
        然後就計算 queue 的第一個元素跟最後一個元素的 index 差值 +1
        """
        if not root: return 0
        ret = 0
        queue = [[root, 0]]
        while queue:
            ret = max(ret, (queue[-1][1] - queue[0][1])+1)
            for i in range(len(queue)):
                c_node, c_idx = queue.pop(0)
                if c_node.left:
                    queue.append([c_node.left, 2*c_idx])
                if c_node.right:
                    queue.append([c_node.right, 2*c_idx+1])
        return ret
