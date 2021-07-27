# 442. Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # revisit 20210726
        counter = Counter(nums)

        output = filter(
            lambda kv:  kv[1] > 1,
            counter.items()
        )
        output = list(zip(*output))
        return output[0] if output else []
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ret = []
        for n in nums:
            idx = abs(n)-1
            if nums[idx] > 0:
                nums[idx] *= -1
            else:
                ret.append(idx+1)

        return ret