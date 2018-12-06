# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        s_counter = [-1]*256
        t_counter = [-1]*256

        for i in range(len(s)):
            if s_counter[ord(s[i])] == t_counter[ord(t[i])]:
                s_counter[ord(s[i])] = i
                t_counter[ord(t[i])] = i
            else: return False

        return True
