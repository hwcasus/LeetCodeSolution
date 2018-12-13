# 140. Word Break II
# https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        memo={}
        def go(s):
            if s in memo: return memo[s]
            if not s: return []
            ret = []
            for w in wordDict:
                if not s.startswith(w): continue
                elif len(w)==len(s): ret.append(w)
                else:
                    rest = go(s[len(w):])
                    print(w, rest)
                    for r in rest:
                        r = w + " " + r
                        ret.append(r)
                    
            memo[s] = ret
            return ret
        
        return go(s)
