#　https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        depth = 0

        while queue:
            size = len(queue)
            depth += 1

            for _ in range(size):
                curr = queue.pop(0)
                if not (curr.left or curr.right):
                    return depth

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

    def minDepth_recursive(self, root: Optional[TreeNode]) -> int:
        def helper(sub_root):
            if not sub_root:
                return 0

            left_depth = helper(sub_root.left)
            right_depth = helper(sub_root.right)

            # if left_depth == 0 and right_depth == 0:
            #     return 1
            # elif left_depth == 0 or right_depth == 0:
            #     return 1 + max(left_depth, right_depth)
            # else:
            #     return 1 + min(left_depth, right_depth)

            return (min(left_depth, right_depth) or (left_depth or right_depth)) + 1

        return helper(root)