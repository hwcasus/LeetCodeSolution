# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/description/

class Solution:
    # 以下根據討論 https://leetcode.com/problems/remove-k-digits/discuss/88678/Two-algorithms-with-detailed-explaination
    # 解決這個問題的時候(或是 Greedy 的問題)
    # 可以先想想如果 k=1 要怎麼做, 最簡單的方法就是掃過整個數列
    # 找出 "峰值"- 也就是比右邊元素還高的值
    # 可以想像一下如果拔掉峰值，就會是右邊那個值來取代他
    # 另外一個想法是，盡可能讓數列保持遞增, 如此一來左邊一定是比較小的數字
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        
        """
        stack = []
        
        kk = k
        for n in num:
            while stack and stack[-1] > n and k > 0:
                k-=1
                stack.pop()
            stack.append(n)
        
        ret = "".join(stack[:len(num)-kk])
        while ret and ret[0] == "0": ret = ret[1:]
        return ret or "0"
