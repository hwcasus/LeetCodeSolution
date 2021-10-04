# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        pace = []

        def helper(sub_root):
            for child in sub_root.children:
                helper(child)

            pace.append(sub_root.val)

        if root:
            helper(root)

        return pace