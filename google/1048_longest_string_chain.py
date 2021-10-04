# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.tmp = dict()

        words.sort(key=len)
        for word in words:
            self.tmp[word] = 1 + max(
                self.tmp.get(word[:i] + word[i+1:], 0)
                for i in range(len(word))
            )

        return max(self.tmp.values())

    def longestStrChaintopdown(self, words: List[str]) -> int:
        self.tmp = dict()

        def helper(word):
            if word in self.tmp:
                return self.tmp[word]

            if word not in words:
                self.tmp[word] = 0
                return 0

            c = 1 + max(
                [
                    helper(word[:i] + word[i+1:])
                    for i in range(len(word))
                ]
            )
            self.tmp[word] = c
            return c

        for word in words:
            helper(word)

        return max(self.tmp.values())