# 889. Construct Binary Tree from Preorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161651/Easy-Python-Recursive-Solution-with-Explanation
        """
        if not pre and not post: return None
        # print(pre, post)
        root = TreeNode(pre[0])
        pre.pop(0)
        post.pop()
        if len(pre) == 1: root.left = TreeNode(pre[0])
        elif pre and post:
            idx = pre.index(post[-1])
            # print(pre[:idx], post[:idx])
            # print(pre[idx:], post[idx:])
            # 只使用一組 idx 是因為要讓他長度一樣
            root.left = self.constructFromPrePost(pre[:idx], post[:idx])
            root.right = self.constructFromPrePost(pre[idx:], post[idx:])
        return root


