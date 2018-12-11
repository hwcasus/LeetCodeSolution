# 31. Next Permutation
# https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        """

        idx = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1] > nums[i]:
                idx=i
                break

        if idx >= 0:
            swap_idx = idx-1
            for i in range(len(nums)-1, idx, -1):
                if nums[idx] < nums[i]:
                    swap_idx = i
                    break
            nums[swap_idx], nums[idx] = nums[idx], nums[swap_idx]
            nums[idx+1:]  = nums[idx+1:][::-1]

        else:
            nums[:]=nums[::-1]
