# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        d = {}
        for n in nums:
            d.setdefault(n, 0)
            d[n] += 1
        
        bucket = {i:[] for i in range(len(nums)+1)}
        for number, frequency in d.items():
            bucket[frequency].append(number)
        
        ret = []
        for i in range(len(nums), -1, -1):
            ret += bucket[i]
            if len(ret) >= k:
                return ret[:k]


    def topKFrequentCounter(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return [key for key, val in Counter(nums).most_common(k)]