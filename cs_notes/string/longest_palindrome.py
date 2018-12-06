# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        c = collections.Counter(s)
        ret = 0
        for k, v in c.items():
            if v > 1:
                ret += (v//2)*2

        return ret+1 if ret < len(s) else ret
