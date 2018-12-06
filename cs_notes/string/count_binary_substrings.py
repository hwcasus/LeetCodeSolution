# 696. Count Binary Substrings
# https://leetcode.com/problems/count-binary-substrings/description/

class Solution:
    # 本題重點可以放在 因為只考慮連續的情況
    # 所以可以利用這個特性, 只要將連續的 0 跟 1 分開，然後兩兩找最小就可以了
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum([min(l[i], l[i+1]) for i in range(0, len(l)-1)])

    def countBinarySubstringsV2(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 1
        ret = []
        for i in range(0, len(s)-1):
            if s[i] != s[i+1]:
                ret.append(c)
                c = 1
            else:
                c+=1
        ret.append(c)

#         cnt = 0
#         for i in range(0, len(ret)-1):
#             cnt += min(ret[i], ret[i+1])
#         return cnt

        return sum([min(ret[i], ret[i+1]) for i in range(0, len(ret)-1)])

    def countBinarySubstringsV1(self, s):
        """
        :type s: str
        :rtype: int
        """

        def pp(s, i, j):
            cnt = 0
            init_l = s[i]
            while i >= 0 and j < len(s) and s[i]!=s[j]:
                if init_l != s[i] : break
                cnt += 1
                i-=1
                j+=1
            return cnt

        cnt = 0

        for i in range(len(s)):
            cnt += pp(s, i, i+1)

        return cnt
