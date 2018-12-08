# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
        這個解法的想法是 
        如果看到重複出現的字而且這個字上次出現在 start 之後
        就表示會重複，所以我要把 start 更新至這個字上次出現的下一個位子
        如此一來就可以避免重複。
        """
        d = {}
        start = ret = 0
        for i, c in enumerate(s):
            if c in d and start <= d[c]:
                start = d[c]+1
            else:
                ret = max(ret, i-start+1)
            d[c] = i
        
        return ret
    
    
    def lengthOfLongestSubstringV1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2: return len(s)
        
        def do(s):
            d = {}
            # total = 0
            l = 0
            for c in s:
                if c in d: break
                else: 
                    d[c] = 1
                    l+=1
            return l
        
        ret = 0
        while s:
            l = do(s)
            s = s[1:]
            ret = max(ret, l)
        return ret
