# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/description/
# https://leetcode.com/problems/palindromic-substrings/discuss/105687/Python-Straightforward-with-Explanation-(Bonus-O(N)-solution)
# https://zh.wikipedia.org/wiki/%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)): dp[i][i] = 1
        for row in range(len(s)-1, -1, -1):
            for col in range(row+1, len(s)):
                if s[row]!=s[col]: continue
                if col == row + 1:
                    dp[row][col] = 1
                else:
                    dp[row][col] = 1 if dp[row+1][col-1]==1 else 0
        
        return sum([sum(row) for row in dp])
    
    
    def countSubstringsSlow(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        def checkIfPalindromic(ss):
            return ss==ss[::-1]
            
            
        for i in range(len(s)+1):
            for j in range(i, len(s)+1):
                count += 0 if i == j else int(checkIfPalindromic(s[i:j]))
        
        return count
    
    
    def countSubstringsSuperSlow(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        def checkIfPalindromic(ss):
            l, h = 0, len(ss)-1
            while l < h:
                if ss[l] != ss[h]:
                    return False
                l+=1
                h-=1
            
            return True
            
            
        for i in range(len(s)+1):
            for j in range(i, len(s)+1):
                count += 0 if i == j else int(checkIfPalindromic(s[i:j]))
        
        return count
    
    
    def countSubstringsFailed(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        def checker(l, h):
            if l < 0 or h > len(s)-1 or h == l: return 0

            count = 1
            ll, hh = l, h
            while ll < hh:
                if s[ll]!=s[hh]:
                    count = 0
                    break
                else:
                    ll+=1
                    hh-=1

            return count + self.checker(s, l+1, h) + self.checker(s, l, h-1)
        
        return checker(0, len(s)-1) + len(s)