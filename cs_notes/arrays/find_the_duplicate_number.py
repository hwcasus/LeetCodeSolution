# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/description/
# https://leetcode.com/problems/find-the-duplicate-number/discuss/191309/Fast-slow-pointers-w-explanation-of-why-there-must-be-one-cycle

class Solution:
    def findDuplicate(self, nums):
        """ 
        :type nums: List[int]
        :rtype: int
        """
        
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = 0
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return sloww