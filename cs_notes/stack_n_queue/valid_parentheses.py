# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if not s: return True
        if len(s)%2 == 1: return False
        
        mapping = {
            '{':1, '}':-1,
            '(':2, ')':-2,
            '[':3, ']':-3,
        }
        
        stack = []
        for c in s:
            #c = stack.pop()
            if not (c in mapping): return False
            if not stack:
                stack.append(c)
            else :
                if mapping[stack[-1]] + mapping[c] == 0:
                    stack.pop()
                elif mapping[c] < 0: ## if right side parentheses didn't match stack.top(), return False
                    return False
                else:
                    stack.append(c)
        return not stack
    
    
    def isValidMe(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if not s: return True
        if len(s)%2 == 1: return False
        
        mapping = {
            '{':'}', '}':'{',
            '(':')', ')':'(',
            '[':']', ']':'[',
        }
        
        stack = []
        for c in s:
            #c = stack.pop()
            if not (c in mapping): return False
            if not stack :
                stack.append(c)
            else :
                if stack[-1] != mapping[c]:
                    stack.append(c)
                else:
                    stack.pop()
        
        return not stack