# https://leetcode.com/problems/recover-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.node = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.node.append(root)
            inorder(root.right)

        inorder(root)
        val = [node.val for node in self.node]

        n = len(val)
        x = y = -1
        for i in range(n - 1):
            if val[i + 1] < val[i]:
                y = i + 1
                if x == -1:
                    x = i
                else:
                    break

        self.node[x].val = val[y]
        self.node[y].val = val[x]

        return root