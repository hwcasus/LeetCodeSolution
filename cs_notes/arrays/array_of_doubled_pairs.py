# 954. Array of Doubled Pairs
# https://leetcode.com/problems/array-of-doubled-pairs/description/

class Solution:
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        獲得提示：數列中最小的數字 x 只需要找 x*2
        所以如果先將數列排序，然後從小到大找他的 x*2 就一定沒問題
        要注意的是，必須是根據絕對值排序

        """

        d = {}
        for a in A: d[a] = d.get(a, 0)+1
        for i, a in enumerate(sorted(A, key=lambda x:abs(x))):
            # print(d)
            if d[a] > 0 and a*2 in d and d[a*2] > 0:
                d[a*2]-=1
                d[a]-=1
        # print(d)

        return all(v == 0 for v in d.values())

    def canReorderDoubledFailedV2(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        d = {}
        for a in A:
            d[a] = d.get(a, 0)+1

        for i, a in enumerate(sorted(A, key=lambda x:abs(x))):
            # print(d)
            if d[a] > 0:
                if type(a/2) is int and a/2 in d and d[a/2] > 0:
                    d[a//2]-=1
                    d[a]-=1
                elif a*2 in d and d[a*2] > 0:
                    d[a*2]-=1
                    d[a]-=1

        return all(v == 0 for v in d.values())

    def canReorderDoubledFailedV1(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        d = {a:False for a in A}

        for i, a in enumerate(A):
            if not d[a]:
                if type(a/2) is int and a/2 in d and not d[a/2]:
                    d[a//2]=True
                    d[a]=True
                elif a*2 in d and not d[a*2]:
                    d[a*2]=True
                    d[a]=True

        return all(list(d.values()))


