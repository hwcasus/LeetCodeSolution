# 179. Largest Number
# https://leetcode.com/problems/largest-number/description/

class Solution:
    # 想像只有兩個數字，如何比較兩者誰先誰後
    # 最簡單的做法就是接起來看看誰比較大
    # 比較大的那個就是正確的大小順序
    #
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        import functools
        l_num = len(nums)
        nums = list(map(str, nums))
        cmp = lambda a,b : -1 if a+b>b+a else 1 if a+b<b+a else 0
        nums.sort(key=functools.cmp_to_key(cmp))
        return str(int("".join(nums)))

    def largestNumberScratch(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        l_num = len(nums)
        nums = list(map(str, nums))

        for i in range(l_num):
            for j in range(0, l_num-i-1):
                if nums[j]+nums[j+1] < nums[j+1]+nums[j] :
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return str(int("".join(nums)))
