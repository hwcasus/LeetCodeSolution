# 459. Repeated Substring Pattern
# https://leetcode.com/problems/repeated-substring-pattern/description/

class Solution:
    def repeatedSubstringPatternSmart(self, s):
        """
        :type s: str
        :rtype: bool
        這個想法比較難想到
        如果是一個重複的字串
        那麼s第一個字必定是重複字串的字首
        那麼s最後一個個字必定是重複字串的字尾
        把s *2 然後把頭跟尾去掉
        假設他是個重複的字串
        就一定會在中間出現s
        """
        return  s in s[1:]+s[:-1]
    
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        這個想法比較務實一點
        就是根據長度判斷如果是重複的，那麼 substring 之長度必定可以整除 string
        從 1 ~ len(s)//2 去找可以整除的值, 將這段substring串接成和string等長
        然後做比較看看是不是一樣的
        """
        for i in range(1, (len(s)//2)+1):
            if len(s)%i==0 and (s[:i]*(len(s)//i) == s): return True
            # if len(s)%i==0: print(s[:i]*(len(s)//i), s)
        return False
                
