# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        # Use set is a little bit faster
        # ret = [] 
        ret = set([])
        def go(current_s, left_n, right_n, state):
            
            if left_n==0 and right_n==0:
                # if current_s not in ret: ret.append(current_s)
                ret.add(current_s)
                return

            if state > 0 and right_n > 0:
                go(current_s+")", left_n, right_n-1, state-1)
            if left_n > 0:
                go(current_s+"(", left_n-1, right_n, state+1)
        
        go("", n, n, 0)
        #return ret 
        return list(ret
                    
    def generateParenthesisDP(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = {1: set(['()']), 2: set(['(())', '()()'])}
        for i in range(3, n+1):
            # pattern 1: outer parenthese + subproblem with length - 1
            dp[i] = set(['(' + x + ')' for x in dp[i-1]])
            for j in range(1, i):
                # pattern 2: dp[i] is formed by dp[j] + dp[i-j]
                dp[i] = dp[i].union([x + y for x in dp[j] for y in dp[i-j]])
        return list(dp[n])