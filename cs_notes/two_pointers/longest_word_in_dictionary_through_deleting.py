# 524. Longest Word in Dictionary through Deleting
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/

class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        
        def is_substring(s, target_s):
            """"Check if target_s is substring of s"""
            
            target_index = 0
            target_len = len(target_s)
            for c in s:
                if target_index == target_len:
                    return True
                if c == target_s[target_index]:
                    target_index += 1
            
            return True if target_index == target_len else False 
        
        ret = ''
        
        for target_s in d:
            if target_s is None or target_s == '':
                continue
            
            if not is_substring(s, target_s):
                continue        
            
            ret_len, target_len =  len(ret), len(target_s)
            if ret_len == target_len:
                if ord(ret[0]) > ord(target_s[0]):
                    ret = target_s
                
            elif ret_len < target_len:
                ret = target_s
                
                
        
        return ret