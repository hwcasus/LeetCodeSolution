# https://leetcode.com/problems/delete-and-earn/

from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        points = [0] * (max(counter) + 1)
        for val in sorted(counter):
            points[val] = val * counter[val]

        prev1 = prev2 = 0
        for p in points:
            prev2, prev1 = prev1, max(prev2 + p, prev1)

        return max(prev1, prev2)