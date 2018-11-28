# 565. Array Nesting
# https://leetcode.com/problems/array-nesting/description/

class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            current, count = i, 0
            while nums[current] != -1: # next value is -1 means have been visited
                nums[current], current = -1, nums[current]
                count += 1
                
            ans = count if count > ans else ans
        return ans
                