"""
Valid Palindrome

https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:

    Input: "race a car"
    Output: false
"""

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l == 0 or l == 1:
            return True
        
        #new_s = ''.join([c for c in s.lower() if c in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'])
        new_s = ''.join([c for c in s.lower() if c in '0123456789abcdefghijklmnopqrstuvwxyz'])
        
        n_l = len(new_s)
        for i in range(n_l):
            if new_s[i] != new_s[-(i+1)]:
                return False
        
        return True