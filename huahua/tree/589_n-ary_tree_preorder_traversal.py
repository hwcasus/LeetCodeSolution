# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        pace = []


        def helper(sub_root):
            pace.append(sub_root.val)
            for child in sub_root.children:
                helper(child)

        if root:
            helper(root)

        return pace