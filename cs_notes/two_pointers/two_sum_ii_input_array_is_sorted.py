# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        sx = 0
        lx = len(numbers)-1
        
        while not(sx > lx):
            current_sum = numbers[sx] + numbers[lx]
            if current_sum == target:
                return [sx+1, lx+1]
            elif current_sum > target:
                lx -= 1
            elif current_sum < target:
                sx += 1