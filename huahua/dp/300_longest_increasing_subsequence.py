# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = [nums[0]]

        for n in nums[1:]:
            if n > seq[-1]:
                seq.append(n)
            else:
                i = 0
                while n > seq[i]:
                    i += 1
                seq[i] = n

        return len(seq)

    def lengthOfLIS_v1(self, nums: List[int]) -> int:
        dp = [1 for _ in nums]

        for idx, n in enumerate(nums):
            cand = [dp[i] for i in range(idx) if nums[i] < n]
            if cand:
                dp[idx] = max(cand) + 1

        return max(dp)