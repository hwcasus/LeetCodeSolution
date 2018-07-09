"""
Longest Common Prefix

https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Note:

    All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        
        min_s = None
        for s in strs:
            if min_s is None:
                min_s = s
            elif len(s) < len(min_s):
                min_s = s
        
        for i in range(0, len(min_s)):
            for s in strs:
                if s.split(min_s[:i+1])[0] != '':
                    return min_s[:i]
        
        return min_s