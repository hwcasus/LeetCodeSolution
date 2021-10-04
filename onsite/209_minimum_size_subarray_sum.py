# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    # 本題想法是直覺是使用 double pointer + sliding windows 去做, 也解的過(v1)
    # 我們可以想像 slow = 0, 然後 iterate over nums, 而 fast 就是 index
    # 然後我們去維持 current_sum = nums[slow:fast]
    # 一開始會是 current_sum = 0, 而隨著 fast 往前,
    # 直到 current_sum >= target, 這個時候就換 slow 往前直到 current_sum < target
    # slow 往前的過程中, 我們去紀錄 (fast - slow) + 1, 就知道目前current_sum長度是多少
    # 透過這個方式就可以找出最短且>= target 的長度
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = 0
        slow = 0
        size = len(nums) + 1

        for fast, num in enumerate(nums):
            current_sum += num
            while current_sum >= target:
                size = min(size, (fast - slow) + 1)
                current_sum -= nums[slow]
                slow += 1

        if size > len(nums):
            return 0

        return size

    def minSubArrayLen_perfect(self, target: int, nums: List[int]) -> int:
        i, res = 0, len(nums) + 1
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                res = min(res, j - i + 1)
                target += nums[i]
                i += 1
        return res % (len(nums) + 1)


    def minSubArrayLen_v1(self, target: int, nums: List[int]) -> int:
        if target <= nums[0]:
            return 1

        slow = fast = 0
        current_sum = nums[0]
        size = len(nums) + 1

        while fast + 1 < len(nums):
            fast += 1
            current_sum += nums[fast]

            while current_sum >= target:
                dist = (fast - slow) + 1
                size = min(size, dist)

                current_sum -= nums[slow]
                slow += 1


        while slow + 1 < len(nums) and current_sum >= target:
            dist = (fast - slow) + 1
            size = min(size, dist)

            current_sum -= nums[slow]
            slow += 1

        return 0 if size > len(nums) else size