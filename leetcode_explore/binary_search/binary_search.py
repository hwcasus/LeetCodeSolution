# 704. Binary Search
# https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low, high = 0, len(nums)-1
        
        while low <= high:
            mid = low + (high - low)//2
            num_mid = nums[mid]
            
            if num_mid == target:
                return mid
            elif num_mid < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
