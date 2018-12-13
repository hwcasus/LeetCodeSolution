# 820. Short Encoding of Words
# https://leetcode.com/problems/short-encoding-of-words/description/

class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        trie = {}
        end = []
        
        words = list(set(words))
        for w in words:
            t = trie
            for c in w[::-1]:
                if c not in t:
                    t[c] = {}
                t = t[c]
            end.append(t)
        
        # 把每個 word 的終點存起來, 如果這個終點有 keys, 就表示說有更長的字包含他
        # 把終點沒 key 的字的(長度+1) 總合起來就是答案
        return sum(len(word)+1 for i, word in enumerate(words) if len(end[i]) == 0)
     
    def minimumLengthEncodingSet(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)
