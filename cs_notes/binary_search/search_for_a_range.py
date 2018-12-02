# 34. Search for a Range
# https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def binary_search(nums, target):
            # Type 2 BS
            left, right = 0, len(nums)
        
            while left < right:
                mid = left + (right - left)//2
                if nums[mid] < target:
                    left = mid +1
                else:
                    right = mid
            return left
        
        start = binary_search(nums, target)
        end = binary_search(nums, target + 1) - 1

        return [-1, -1] if start > end else [start, end]

    def searchRangeNotGood(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        
        start = left
            
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        
        end = right
        return [-1, -1] if start > end else [start, end]
