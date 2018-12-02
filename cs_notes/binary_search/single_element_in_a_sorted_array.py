# 540. Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + (right-left)//2
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    left = mid + 1                
                else:
                    right = mid                   
            else:
                if nums[mid-1] == nums[mid]:
                    left = mid +1            
                else:
                    right = mid
        return nums[left]
    
    
    def singleNonDuplicateDetail(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        
        print('left\tmid\tright')
        while left < right:
            mid = left + (right-left)//2
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    print('{}\t{}\t{}, single 在 mid 右邊'.format(left, mid, right))
                    left = mid + 1
                    
                else:
                    print('{}\t{}\t{}, single 在 mid 左邊'.format(left, mid, right))
                    right = mid                   
            else:
                if nums[mid-1] == nums[mid]:
                    print('{}\t{}\t{}, single 在 mid 右邊'.format(left, mid, right))
                    left = mid +1
                    
                else:
                    print('{}\t{}\t{}, single 在 mid 左邊'.format(left, mid, right))
                    right = mid
                    
        print('{}\t{}\t{}, 出來了'.format(left, mid, right))
        return nums[left]
        
            
