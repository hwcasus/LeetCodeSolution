# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/description/

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # len(self.sums) would be len(nums)+1
        # which means that self.sum[i] = sum from 0 to i
        self.sums = [0]
        for n in nums: self.sums.append(self.sums[-1]+n)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # i and j are 0-indexed
        # sum of range(3 , 5) means 4th and 6th element
        # sum from 0 to 6 - sum from 0 - 3 = sum from 4 - 6
        # = sum[6]-sum[3]
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
