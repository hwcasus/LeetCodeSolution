# 268. Missing Number
# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return int(n*(n+1)/2) - sum(nums)
    
    def missingNumberBitwise(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ret = 0
        for i, n in enumerate(nums):
            ret = ret ^ i ^ n

        return ret ^ len(nums)