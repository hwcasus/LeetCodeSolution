# https://leetcode.com/problems/number-of-longest-increasing-subsequence/


class Solution:
    def findNumberOfLIS_me(self, nums: List[int]) -> int:
        dp_count = [1 for _ in nums]
        dp_len = [1 for _ in nums]

        for idx in range(1, len(nums)):
            candidate = Counter() # key: len, val: count
            for i in range(idx):
                if nums[idx] > nums[i]:
                    candidate[dp_len[i]+1] += dp_count[i]

            if candidate:
                dp_len[idx] = max(candidate.keys())
                dp_count[idx] = candidate[dp_len[idx]]

        a = max(dp_len)
        return sum([count for count, length in zip(dp_count, dp_len) if length == a])
