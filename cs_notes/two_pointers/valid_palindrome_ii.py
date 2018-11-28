# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_palindrome(s, h, t):
            while (h < t):
                if s[h] != s[t]:
                    return False
                h+=1
                t-=1
            return True
        
        h = -1
        t = len(s)
        while(h < t):
            h+=1
            t-=1
            if s[h] != s[t]:
                return is_palindrome(s, h, t-1) or is_palindrome(s, h+1, t)
        return True
        
        