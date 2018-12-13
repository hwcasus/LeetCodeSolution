# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/description/

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        cnt = collections.Counter(words)
        # 預設為從小到大, 所以加負號
        heap = [(-freq, word) for word, freq in cnt.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
    
    def topKFrequentSort(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import collections
        cnt = collections.Counter(words)
        keys = list(cnt.keys())
        # 預設為從小到大將 cnt 轉負數
        # 另外英文字母也是比較小放前面
        keys.sort(key=lambda w: (-cnt[w], w)) 
        return keys[:k]

