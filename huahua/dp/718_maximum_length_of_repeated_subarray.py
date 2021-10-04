# 718. Maximum Length of Repeated Subarray

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums1) + 1)] for _ in range(len(nums2) + 1)]

        ret = 0
        for row, num2 in enumerate(nums2):
            for col, num1 in enumerate(nums1):
                if num2 == num1:
                    dp[row+1][col+1] = dp[row][col] + 1
                    ret = max(ret, dp[row+1][col+1])


        return ret

