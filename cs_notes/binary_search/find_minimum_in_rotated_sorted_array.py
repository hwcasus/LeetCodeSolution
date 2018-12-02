# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]
