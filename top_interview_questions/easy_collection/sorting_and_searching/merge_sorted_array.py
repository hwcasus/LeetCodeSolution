#   Merge Sorted Array
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        while n > 0 or m >= 0:
            if n-1 < 0:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            elif m-1 < 0:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            elif nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1


        # nums1_idx = m-1
        # nums2_idx = n-1
        # nums1_end_idx = m+n-1
        
        # while nums2_idx >= 0 or nums1_idx >= 0:
            
        #     if nums2_idx < 0:
        #         nums1[nums1_end_idx] = nums1[nums1_idx]
        #         nums1_idx -= 1
        #     elif nums1_idx < 0:
        #         nums1[nums1_end_idx] = nums2[nums2_idx]
        #         nums2_idx -= 1
        #     elif nums2[nums2_idx] >= nums1[nums1_idx]:
        #         nums1[nums1_end_idx] = nums2[nums2_idx]
        #         nums2_idx -= 1
        #     else:
        #         nums1[nums1_end_idx] = nums1[nums1_idx]
        #         nums1_idx -= 1
                
        #     nums1_end_idx -= 1