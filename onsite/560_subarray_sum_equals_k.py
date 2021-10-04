# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 本題重點為結合 prefix sum 和 cache
        # 簡單來說就是
        # 1. 走過 nums 並計算累計和
        # 2. 將當前累計和放進 cache, 並檢查目前 cache 中是否有 累計和 - k
        #    若有則表示 之前曾經出現過該累計和, 也就意味著
        #    目前累計和扣掉曾出現的部分, 總和就會等於 k

        cache = {0: 1}
        current_sum = 0
        ans = 0
        for n in nums:
            current_sum += n
            ans += cache.get(current_sum - k, 0)
            cache[current_sum] = cache.get(current_sum, 0) + 1

        return ans


    def subarraySum_v1(self, nums: List[int], k: int) -> int:
        ans = 0
        start = 0
        current_sum = 0

        for n in nums:
            current_sum += n
            while current_sum > k:
                current_sum -= nums[start]
                start += 1
            if current_sum == k:
                ans += 1

        return ans

    def subarraySum_v2(self, nums: List[int], k: int) -> int:
        dp = [0]
        for n in nums:
            dp.append(dp[-1] + n)
        dp.pop(0)

        ans = 0
        for i in range(len(dp)):
            if dp[i] == k:
                ans += 1
            for j in range(i):
                if dp[i] - dp[j] == k:
                    ans += 1

        return ans
