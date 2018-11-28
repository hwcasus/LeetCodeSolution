# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums)[::-1][k-1]

    def findKthLargestHeapSort(self, nums, k):
        from heapq import *
        heap = nums[:k]
        heapify(heap)
        
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heappushpop(heap, nums[i])
        
        return heap[0]

    def findKthLargestQuickSort(self, nums, k):
            """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def quicksort(i, j):
            rand_index = random.randint(i, j)
            nums[rand_index], nums[j] = nums[j], nums[rand_index]
            pivot_index, pivot_val = i, nums[j]
            for k in range(i, j):
                if nums[k] > pivot_val:
                    nums[k], nums[pivot_index] = nums[pivot_index], nums[k]
                    pivot_index += 1
            nums[pivot_index], nums[j] = nums[j], nums[pivot_index]
            return pivot_index

        i, j = 0, len(nums) - 1
        while i < j:
            m = quicksort(i, j)
            if m == k - 1:
                return nums[m]
            if m < k:
                i = m + 1
            else:
                j = m - 1
        return nums[i]

    def findKthLargestQuickSelect(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def partition(nums, head, tail):
            pivot = nums[tail]
            left, right = head, tail-1
            
            while left <= right:
                while nums[left] <= pivot and left < tail: left += 1
                while nums[right] >= pivot and right > head: right -= 1
                if left >= right: break # This line is quite critical.
                    
                nums[left], nums[right] = nums[right], nums[left]
            nums[tail], nums[left] = nums[left], nums[tail]

            return left
        
        n_len = len(nums)
        k = n_len - k # 找第 k 大的值 = 找從排序之後的後面數過來第 k 個值
        head, tail = 0, n_len-1
        
        while head < tail:
            pivot_index = partition(nums, head, tail)
            if pivot_index == k:
                break
            elif pivot_index < k:
                head = pivot_index + 1
            else:
                tail = pivot_index - 1
            
        return nums[k]
