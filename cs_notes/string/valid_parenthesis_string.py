# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/description/

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        這個 greedy 的解法的想法是在 pass 整個字串的過程中
        去計算當前的 `balance`, 所謂的 balance 
        就是把'('當成+1, 把')'當成-1, 把字串轉換成一個數字的意思
        一個合法的括號方式，從 0 開始的子字串之 balance 必定大於 0
        (balance 大於 0 的意思其實就是左括號比右括號多的意思)
        而這題又多了一個萬能字元 - 星號，所以我們不能只計算 balance
        要考慮 balance 可能的最大值及最小值
        也就是說
            '(' 會使 最大值跟最小值都 +1
            ')' 會使 最大值跟最小值都 -1
            '*' 會使 最大值 +1 而最小值 -1
        過程中，只要最大值沒有 == 0 就沒關係
        最小值每次要經過 max(0, 最小值), 確保其 >0
        這個動作的前提是最大值要是大於0的
        只要最大值大於0, 就表示目前還有機會是合法的括號字串
        所以如果要往後再接一個, 必定是基於合法的往後接
        不可能是基於一個 balance = -1 的字串繼續計算 balance
        所以最小值如果小於0 就一定要重製成 0
        最後跳出迴圈的時候，如果最大值是 > 0 而且最小值 <= 0
        就會是正確的，這個條件之所以要求最小值 <= 0 是因為
        必須讓最大值跟最小值之間包含 0, 因為合法的括號字串 balance 只能為 0
        假若看過最後一個字母後, 最小值 > 0, 這代表我們有太多左括號
        經過 low = max(low, 0) 依然會是 > 0
        但如果 low 是負的且 high 是正的, low = max(low, 0) 就會是 0
        """
        low = high = 0
        for c in s:
            low += 1 if c == '(' else -1
            high += 1 if c in '(*' else -1
            if high < 0: break
            low = max(low, 0)
        
        return low==0
            
    def checkValidStringFailed(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def go(s, stack):
            for i in range(len(s)):
                if s[i] == '(':
                    stack.append(s[i])
                elif s[i] == ')':
                    if not stack: return False
                    stack.pop()
                else:
                    return (go(s[i:], stack+['(']) or  go(s[i:], stack+[')']) or go(s[i:], stack))
            
            return len(stack) == 0
        
        stack = []
        return go(s, stack)
        
