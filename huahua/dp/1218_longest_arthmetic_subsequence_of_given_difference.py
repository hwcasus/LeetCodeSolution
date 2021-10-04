# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution:
    # 這題挺難的
    def longestSubsequence2(self, arr: List[int], difference: int) -> int:
        accumu_len = [1] * len(arr)
        current_maximum = 1
        for i in range(1, len(arr)):
            for j in range(0, i):
                if arr[j] + difference == arr[i]:
                    accumu_len[i] = max(accumu_len[i], accumu_len[j] + 1)
                    current_maximum = max(current_maximum, accumu_len[i])

        return current_maximum

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp_map = {arr[0]: 1}
        current_maximum = 0
        for num in arr[1:]:
            dp_map[num] = dp_map.get(num-difference, 0) + 1
            current_maximum = max(current_maximum, dp_map[num])

        return current_maximum