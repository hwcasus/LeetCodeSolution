# 139. Word Break
# https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[0]=True
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    # print(dp[j], s[j:i], j, i)
                    dp[i]=True
        
        # print(dp)
        return dp[-1]
