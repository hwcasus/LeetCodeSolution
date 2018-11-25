# 15. 3Sum
# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        list.sort(nums)
        print (nums)
        result = []
        for i, first in enumerate(nums[:-1]):
            # this line prevent we use same FIRST
            if i > 0 and nums[i] == nums[i-1]: continue
            head, tail = i+1, len(nums)-1
            while head < tail:
                second, third = nums[head], nums[tail]
                sec_n_thr = -(second + third)
                if first < sec_n_thr:
                    head += 1
                elif first > sec_n_thr:
                    tail -= 1
                else:
                    result += [[first, second, third]]
                    # this line prevent we use same SECOND
                    while (head < tail and nums[head]==nums[head+1]):head += 1
                    # this line prevent we use same THIRD
                    while (head < tail and nums[tail]==nums[tail-1]):tail -= 1
                    head += 1
                    tail -= 1
                    
        return result
