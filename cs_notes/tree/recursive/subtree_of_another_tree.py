# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/description/

class Solution:
    def isSubtree(self, s, t):
        if not s: return False
        
        def to_str(n):
            return '^' + str(n.val) + '/' + to_str(n.left) +'\\'+ to_str(n.right) if n else '#'

        return to_str(t) in to_str(s)
    
    def isSubtreeNonOpt(self, s, t):
        
        def to_str(n):
            return '^' + str(n.val) + '/' + to_str(n.left) +'\\'+ to_str(n.right) if n else '#'

        def traveler(s, t_str):
            if not s: return False
            return t_str in to_str(s) 
            # following line still make new string each time when go to new node.
            # return t_str == to_str(s) or traveler(s.left, t_str) or traveler(s.right, t_str)
        
        return traveler(s, to_str(t))
    
    def isSubtreeRecursice(self, s, t):
        """ This function would travel all node and use each node as root to check if t is subtree of s
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        return self.isSubtreeRoot(s, t) or self.isSubtreeRecursice(s.left, t) or self.isSubtreeRecursice(s.right, t) if s else False
    
    def isSubtreeRoot(self, s, t):
        """ This function check if t is subtree of s which is start from s.
        """
        if bool(s) != bool(t): return False
        return (s.val == t.val and self.isSubtreeRoot(s.left, t.left) and self.isSubtreeRoot(s.right, t.right)) if s else True
        
    