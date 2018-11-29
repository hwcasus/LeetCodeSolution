# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_idx = -1
        for c in s:
            # plus one means that finding c from the right-side of last word index you find 
            s_idx = t.find(c, s_idx+1)
            if s_idx == -1:
                return False
        
        return True
    
    def isSubsequenceRough(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        s_idx = 0
        s_len = len(s)
        for c in t:
            if s_idx == s_len:
                return True
            if s[s_idx] == c:
                s_idx += 1
        
        return s_idx == s_len