# https://leetcode.com/problems/top-k-frequent-elements/

import itertools

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 本題重點為 bucket
        # 先走過所有 num, 計算出現次數
        # 接著再用另外一個 array , 將出現次數相同的 element 放在一起
        # 再由出現次數大到小的方式去把 array 串起來
        # 最後回傳 串起來之後的 array 的前 k 個 element

        records = {}
        for n in nums:
            records[n] = records.get(n, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for num, count in records.items():
            freq[count].append(num)

        flat_freq = list(itertools.chain(*freq))
        return flat_freq[::-1][:k]