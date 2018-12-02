# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        start, end = 0, len(nums)-1
        
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid]==target:
                return mid
            if nums[mid] < nums[end]:
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid -1
            else:
                if nums[start] <= target and target < nums[mid]:
                    end = mid -1
                else:
                    start = mid + 1
        
        return -1
    def searchDetail(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        start, end = 0, len(nums)-1
        
        # print('start\tmid\tend')
        while start <= end:
            mid = start + (end - start)//2
            if nums[mid]==target:
                # print('{}({})\t{}({})\t{}({})'.format(start, nums[start], mid, nums[mid], end, nums[end]))
                return mid
            if nums[mid] < nums[end]:
                if nums[mid] < target and target <= nums[end]:
                    # print('{}({})\t{}({})\t{}({}), 右邊有序, k 介於 mid 和 end 之間'\
                    # .format(start, nums[start], mid, nums[mid], end, nums[end]))
                    start = mid + 1
                else:
                    # print('{}({})\t{}({})\t{}({}), 左邊無序, k 介於 start 和 mid 之間'\
                    # .format(start, nums[start], mid, nums[mid], end, nums[end]))
                    end = mid -1
            else:
                if nums[start] <= target and target < nums[mid]:
                    # print('{}({})\t{}({})\t{}({}), 左邊有序, k 介於 start 和 mid 之間'\
                    # .format(start, nums[start], mid, nums[mid], end, nums[end]))
                    end = mid -1
                else:
                    # print('{}({})\t{}({})\t{}({}), 右邊無序, k 介於 mid 和 end 之間'\
                    # .format(start, nums[start], mid, nums[mid], end, nums[end]))
                    start = mid + 1
        
        # print('{}({})\t{}({})\t{}({})'.format(start, nums[start], mid, nums[mid], end, nums[end]))
        return -1 #if nums[start]!=target else start
                    
        
