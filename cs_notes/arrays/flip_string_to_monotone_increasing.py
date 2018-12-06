# 926. Flip String to Monotone Increasing
# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/

class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        這個解法的想法是，最終我們希望S變成以下三種狀況之一
        1) 全都 1
        2) 全都 0
        3) 從某個元素開始，前面全都 0, 後面全都 1
        先討論 3), 假設我們要從第 i 個元素開始把 S 翻成 ith 前面全都 0, ith 後面全都1
        而從 i 開始翻的次數必然是取決於 `i 前面有多少個 1` + `i 後面有多少個 0`
        所以下面我們使用 zs(zeroes) 及 os(ones) 來紀錄, 這兩個陣列長度都是 len(S)+1,
        zs[i]負責記錄在 ith 之後還有幾個0; os[i]則記錄 ith 之前有多少個 1, 紀錄完之後
        zs[1] 就表示第一個元素後面全都翻成1 要翻多少次, 其實也就是 (1)
        而 os[-1] 就表示最後一個元素前面全都翻成0 要翻多少次, 其實也就是 (2)
        所以只要把這個 zs, os 相加的最小值找出來後, 再比較三者的最小值, 就可以取得答案了
        """
        zs, os = [S.count('0')], [0]
        c_min = float('inf')

        for s in S:
            zs.append(zs[-1]-int(s=='0'))
            os.append(os[-1]+int(s=='1'))
            c_min = min((zs[-1]+os[-1]), c_min)
        # c_min = min([zs[i] + os[i] for i in range(1, len(S))])
        return min(zs[1], os[-1], c_min)

    def minFlipsMonoIncrFailed(self, S):
        """
        :type S: str
        :rtype: int
        """
        while S and S[0] == '0': S = S[1:]
        if not S: return 0
        while S and S[-1] == '1': S = S[:-1]
        if not S: return 0
        print(S)
        return min(S.count('1'), S.count('0'))
