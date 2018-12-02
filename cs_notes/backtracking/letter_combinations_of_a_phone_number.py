# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0: return []
        
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        ret = []
        
        def go(current_s, nxt_digits_idx):
            if nxt_digits_idx == len(digits):
                ret.append(current_s) 
                return
            for nxt_c in letters[int(digits[nxt_digits_idx])]:
                go(current_s+nxt_c, nxt_digits_idx+1)
        
        go("", 0)
        return ret
    
    def letterCombinationsString(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ret = ['']
        
        for num in digits[::-1]:            
            ret = [c + current_s for c in letters[int(num)] for current_s in ret]
        return ret
