# 566. Reshape the Matrix
# https://leetcode.com/problems/reshape-the-matrix/description/

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        old_r, old_c = len(nums), len(nums[0])
        if old_r * old_c != r * c: return nums
        
        ret = []
        tmp = []
        for rows in nums:
            for cols in rows:
                tmp.append(cols)
                if len(tmp) == c:
                    ret.append(tmp)
                    tmp = []
        
        return ret