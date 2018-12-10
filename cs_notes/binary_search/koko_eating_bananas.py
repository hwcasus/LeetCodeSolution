# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        典型的type 2
        """
        if H <= len(piles): return max(piles)

        def is_affordable(k): return sum(((p-1)//k)+1 for p in piles) <= H

        low, high = 1, max(piles)
        while low < high:
            mid = low + (high-low)//2
            if is_affordable(mid):
                high = mid
            else:
                low = mid+1

        return low

    def minEatingSpeedFailed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        我的版本，多做了 sort 但其實沒啥用
        然後這個不是 type 2
        type 2 不會有 == 的條件式
        最後外面回傳 low
        """

        if H <= len(piles): return max(piles)

        piles.sort()
        low, high = 1, piles[-1]

        while low < high: # stop when low == high
            mid = low + (high-low)//2
            s = 0
            for p in piles:
                a, b = divmod(p, mid)
                s += a + int(b>0)

            print('{}\t{}\t\t{}\t{}\t{}'.format(s, H, low, mid, high))
            if s == H:
                return mid if mid in piles else low
            elif s > H: # 吃太慢
                low = mid+1
            else:
                high = mid

        return mid

