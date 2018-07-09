"""
Valid Anagram
 
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:

    Input: s = "rat", t = "car"
    Output: false

Note:

    You may assume the string contains only lowercase alphabets.

Follow up:

    What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        d = {}
        for c in s:
            if c in d:
                d[c]+=1
            else:
                d[c] = 1
                
        for c in t:
            if c in d:
                d[c]-=1
                if d[c] < 0:
                    return False
            else:
                return False
        
        return True