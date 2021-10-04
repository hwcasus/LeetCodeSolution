# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        accumulated_nums = [0] * len(nums)
        accumulated_nums[0] = nums[0]
        for i in range(1, len(nums)):
            accumulated_nums[i] = accumulated_nums[i-1] + nums[i]

        self.accumulated_nums = accumulated_nums

    def sumRange(self, left: int, right: int) -> int:
        if right == 0:
            return self.accumulated_nums[0]
        elif left == 0:
            return self.accumulated_nums[right]
        else:
            return self.accumulated_nums[right] - self.accumulated_nums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)