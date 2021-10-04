# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1

        for element in nums[1:]:
            if count == 0:
                candidate = element

            count += (1 if element == candidate else -1)

        return candidate
