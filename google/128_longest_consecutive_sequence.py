# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest_len = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set: # get the start of sequence
                sequence_len = 1
                current_num = num
                while current_num + 1 in nums_set:
                    current_num += 1
                    sequence_len += 1

                longest_len = max(longest_len, sequence_len)


        return longest_len