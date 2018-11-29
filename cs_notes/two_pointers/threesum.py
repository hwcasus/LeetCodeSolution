# 15. 3Sum
# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        list.sort(nums)
        result = []
        for i, first in enumerate(nums[:-1]):
            # this line prevent we use same FIRST
            if i > 0 and nums[i] == nums[i-1]: continue
            head, tail = i+1, len(nums)-1
            while head < tail:
                second, third = nums[head], nums[tail]
                sec_n_thr = -(second + third)
                if first < sec_n_thr:
                    head += 1
                elif first > sec_n_thr:
                    tail -= 1
                else:
                    result += [[first, second, third]]
                    # this line prevent we use same SECOND
                    while (head < tail and nums[head]==nums[head+1]):head += 1
                    # this line prevent we use same THIRD
                    while (head < tail and nums[tail]==nums[tail-1]):tail -= 1
                    head += 1
                    tail -= 1
                    
        return result

    def threeSumFailed(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def get_rest(nums, s):
            i, j = s
            cnums = [n if nx>j else None for nx, n in enumerate(nums)]
            return cnums

        two_sum = []
        two_sum_idx = []

        for ix, i in enumerate(nums):
            for jx, j in enumerate(nums[ix+1:]):
                two_sum += [i+j]
                two_sum_idx += [(ix, ix+jx+1)]

        threesum = []
        candi = []

        for tsx, ts in enumerate(two_sum):
            ix, jx = two_sum_idx[tsx]
            ans = [ts + n if nx>jx else None for nx, n in enumerate(get_rest(nums, (ix, jx)))]
            ans_idx = [[nums[ix], nums[jx], n]if nx>jx else None for nx, n in enumerate(get_rest(nums, (ix, jx)))]

            candi += [ans_idx[ax] for ax, a in enumerate(ans) if a==0]

        for c in candi:
            flag = True
            if len(threesum) ==0:
                threesum+=[c]
            else:
                for a in threesum:
                    if set(c) == set(a):
                        flag = False

                if flag: 
                    threesum+=[c]


        return threesum