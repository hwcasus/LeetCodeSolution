"""
Remove Duplicates from Sorted Array

https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

    Given nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

    It doesn't matter what you leave beyond the returned length.

Example 2:

    Given nums = [0,0,1,1,1,2,2,3,3,4],

    Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

    It doesn't matter what values are set beyond the returned length.

"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (nums is None) or (not nums):
            return 0
        
        l = len(nums)
        if l == 1:
            return 1
        
        s = 0
        e = 1
        while True:
            l = len(nums)
            if e >= l:
                return l
            
            if nums[s] != nums[e]:
                s+=1
                e+=1
            else:
                while (nums[s] == nums[e]):
                    e += 1
                    if e == l:
                        break
                del nums[s:e-1]
                s += 1
                e = s + 1