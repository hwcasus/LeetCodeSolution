# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums):
        """ This is so cool.
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        l = r = 1
        output = [1]*n
        
        for i in range(n):
            output[i] *= l
            l *= nums[i]
            
        for i in range(n-1, -1, -1):
            output[i] *= r
            r *= nums[i]
        
        return output
        
    def productExceptSelfSlow(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = [1]*len(nums)
        
        for i, n in enumerate(nums):
            for j in range(len(result)):
                if i != j:
                    result[j]*=n
            
        return result