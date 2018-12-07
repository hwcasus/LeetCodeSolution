# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""
        def is_palindrome(s, i, j):
            local_ret = None
            while i >= 0 and j < len(s) and s[i] == s[j]:
                local_ret = s[i:j+1]
                i-=1
                j+=1

            return local_ret

        ret = ""
        for i in range(len(s)):
            a = is_palindrome(s, i, i)
            b = is_palindrome(s, i, i+1)
            if a and len(a) > len(ret): ret = a
            if b and len(b) > len(ret): ret = b
        return ret
