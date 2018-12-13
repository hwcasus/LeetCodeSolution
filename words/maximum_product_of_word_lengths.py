# 318. Maximum Product of Word Lengths
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/

class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        本題解法為
        可以 abcdef 轉換成 mask
        舉例來說可以用 list 實現, 就是 [1, 1, 1, 1, 1, 1, 0, ...]
        但這邊改用 binary int 實現,
        也就是 abcdef = 0b111111, acf = 0b100101
        好處就是可以透過 & 運算比較兩個單字是否有重疊
        如果兩個 mask & 是 0 就表示, 沒有任何一個字母重疊
        """
        
        masks = []
        for w in words:
            mask = 0
            for c in w:
                digit = ord(c) - ord('a')
                mask = mask | (1 << digit)
            masks.append(mask)
        
        ret = 0
        for i in range(len(masks)):
            for j in range(i+1, len(masks)):
                if not (masks[i]&masks[j]):
                    ret = max(ret, len(words[i])*len(words[j]))
        
        return ret
                
