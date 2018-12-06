# 916. Word Subsets
# https://leetcode.com/problems/word-subsets/description/

class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        這邊的解法將 V1 精簡化, 但核心想法還是一樣的
        total_dict 就是 B 的要求，但不同於長度為 26 的 list
        這邊只記錄了字母數 > 0 的字母，所以後面再檢驗 a 的時候會比較快
        另外也利用了 count function 加速
        """

        total_dict = {}
        for b in B:
            for c in b:
                total_dict.setdefault(c, 0)
                total_dict[c] = max(b.count(c), total_dict[c])

        def a_compare_total(a, d):
            for char, count in d.items():
                if a.count(char) < count: return False
            return True

        return [a for a in A if a_compare_total(a, total_dict)]

    def wordSubsetsV1(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        這邊解法的想法是分成 3 個步驟
        1) 求出每個 b 的要求
        2) 整合 B 的最低要求
        3) 檢查每個 a 是否符合 B 的最低要求
        """

        # 1)
        def to_count(s):
            ret = [0]*26
            for c in s: ret[ord(c)-ord('a')]+=1
            return ret

        # 2)
        total_sum = [0]*26
        for b_count in map(to_count, B):
            total_sum = list(map(max, zip(total_sum, b_count)))

        # 3)
        def a_compare_total(a, t_sum):
            for a, b in zip(to_count(a), t_sum):
                if a < b: return False
            return True

        return [a for a in A if a_compare_total(a, total_sum)]
