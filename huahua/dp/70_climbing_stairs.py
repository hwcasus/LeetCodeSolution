# https://leetcode.com/problems/climbing-stairs/
class Solution:
    # 這次我很快就想到了費式數列
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        cache = [0] * (n + 1)
        cache[1] = 1
        cache[2] = 2
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n]
