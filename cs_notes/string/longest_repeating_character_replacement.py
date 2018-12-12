# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        核心概念是運用 sliding windows
        可以先從假設 k 沒有限制開始想
        如果 k 沒有限制但希望用最少次, 那一定是找當前出現最多次的字
        然後將 string 全長 - 最多次的字的出現次數就是答案
        但現在有長度限制，所以我們從子字串 [start:end] = [0:0] 開始探索
        為了方便解釋，以下將"當前出現最多次的字的次數"稱為 max_char_count
        如果目前子字串長度扣掉 max_char_count 還小於等於 k, 就表示我還可以接受下一個字, 將 end += 1
        如果超過了，也就是當前子字串長度 > max_char_count + k, 就表示目前這個字串只用k次沒辦法改了
        我就持續將目前 start 的字從紀錄中扣掉，然後 start += 1
        直到滿足 (end-start+1) < max_char_count + k 才回到增加 end 的流程
        而每次增加 end 之前，都對當前長度進行比較，留下最大值，最後進行回傳即可
        
        """
        count=[0]*26
        def ascii_idx(c): return ord(c)-ord('A')
        start = max_char_count = max_len = 0
        
        for end in range(len(s)):
            # 每次將 end 往後一步
            count[ascii_idx(s[end])] += 1
            # 將被新增的字的出現數量跟當前最大做比較
            max_char_count = max(max_char_count, count[ascii_idx(s[end])])
            # 如果目前出現最多的字的數量 + 替換量 k < 目前長度
            # 就表示目前這個長度的 string 是沒辦法藉由抽換 k 個字來使其變成只有單一種字的
            while (end-start+1) > k + max_char_count:
                # 那就更新字的counter 並讓 start 往前走, 直到目前是可以接受的
                count[ascii_idx(s[start])] -= 1
                start += 1
            # 試著比較看看目前長度跟看過的最大長度哪個比較大
            max_len = max(max_len, end-start+1)
        
        return max_len
