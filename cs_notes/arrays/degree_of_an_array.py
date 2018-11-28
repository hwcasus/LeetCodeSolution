# 697. Degree of an Array
# https://leetcode.com/problems/degree-of-an-array/description/

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return nums
        
        # collections.counter just work the exactly same way
        cnt = {}
        for n in nums:
            cnt.setdefault(n, 0)
            cnt[n]+=1
        max_count = max(cnt.items(), key=(lambda key: cnt[key[0]]))[1]
        if max_count == 1: return 1
        
        candidates = [k for k, d in cnt.items() if d == max_count]
        
        len_n = len(nums)
        ret = 50001
        
        for c in candidates:
            l = nums.index(c)
            r = len_n - nums[::-1].index(c) -1 # to get correct idx
            ret = min(ret, r - l + 1)
            
        return ret
    
    def findShortestSubArrayRough(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return nums
        
        head, cnt, tail = {}, {}, {}
        len_rec, current_cnt = 50001, 0
        
        for i, n in enumerate(nums):
            head.setdefault(n, i)
            cnt.setdefault(n, 0)
            
            tail[n] = i
            cnt[n] += 1    
            new_len = i - head[n] + 1
            if cnt[n] > current_cnt or (cnt[n] == current_cnt and len_rec > new_len):
                print(head[n], tail[n], new_len)
                len_rec = new_len
                current_cnt = cnt[n]
        return len_rec