# 645. Set Mismatch (Easy)
# https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len_n = len(nums)
        correct_sum = (len_n*(len_n+1))//2
        actual_sum = 0
        duplicate_num = 0
        
        for n in nums:
            real_idx = abs(n)-1
            if nums[real_idx] > 0: 
                nums[real_idx] *= -1
            else:
                duplicate_num = real_idx+1
            actual_sum += (real_idx+1)
        
        return [duplicate_num, correct_sum - (actual_sum - duplicate_num)]

    
    def findErrorNumsCool(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0, 0]
        for n in nums:
            # mapping number to (sorted) index
            idx = abs(n)-1
            # only the index corresponded with duplicate number would possibly be negative 
            # because it's duplicate
            if nums[idx] > 0: 
                nums[idx] *= -1
            else:
                res[0] = idx+1 # mapping index to number
        
        for i, n in enumerate(nums):
            # only the index corresponded with missing number would be positive
            # since it has never been visited
            if n > 0:
                res[1] = i+1
                return res
        
    def findErrorNumsPythonicAndFaster(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = sum(nums)
        n = len(nums)
        duplicate = s - sum(set(nums))
        missing = duplicate + int(((n*(n+1))/2)-s)
        return [duplicate, missing]