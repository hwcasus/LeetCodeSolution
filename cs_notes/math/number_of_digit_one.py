# 233. Number of Digit One
# https://leetcode.com/problems/number-of-digit-one/description/

class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        關鍵在於每個位數分開找, 例如 n = 38415
        萬位 3 會出現 10000 次的 1 (10000-19999)
        千位 8 會出現  4000 次的 1 (1000-1999, 11000-11999, 21000-21999, 31000-31999)
        百位 4 會出現  3900 次的 1 (100-199, ..., 1100-1199, ..., 38100-38199)
        十位 1 會出現  3846 次的 1 (11-19, ..., 1010-1019, ......, 38410-38415)
        個位 1 會出現  3842 次的 1 (1, 11, 21, ..., 20001, 20011, ..., 38411 )
        目前位數若等於 0, 次數為 "目前位數左邊的數字" 乘 "位數值"
        目前位數若等於 1, 次數為 "目前位數左邊的數字" 乘 "位數值" 加上 "目前位數右側的值加 1"
        目前位數若大於 1, 次數為 "目前位數左邊的數字加 1" 乘 "位數值"

        可以將包含目前位數到最左側稱為 left, 目前位數右側稱為 right ,
        而目前位數值 (10的幾次方) 稱為 current_digit, 則可以將規則整理成
            (left + 8) / 10 * current_digit + (left % 10 == 1) * (right+ 1)
        """
        d = 1
        ret = 0
        while d <= n:
            left, right = divmod(n, d)
            ret += (left + 8)//10*d
            if left % 10 == 1: ret += right+1
            d *= 10
        return ret

