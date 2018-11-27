# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        top = 0
        for n in nums:
            if n:
                idx += 1
            else:
                # top = max(top, idx) # max is slower than if statement
                top = top if top > idx else idx
                idx = 0 
        return top if top > idx else idx
        #return max(top, idx)