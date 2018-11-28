# 769. Max Chunks To Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted/description/

class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        current_max = -1
        count = 0
        for i, n in enumerate(arr):
            if current_max < n: current_max = n
            # n == i 表示排序之後所有元素都會在適當的位子上, nums[i] = n for all what we've seen
            # 例如：如果在 n[0, 1, 2, 3] 中 最大值是4 就表示裡面一定是1, 2, 3, 4 所以排序就沒問題
            if current_max == i: count += 1
        
        return count