# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain_bottom_up(self, words: List[str]) -> int:

        seen = {}
        words.sort(key=len)

        for word in words:
            seen[word] = max(
                seen.get(word[:i] + word[i+1:], 0)
                for i in range(len(word))
            ) + 1

        return max(seen.values())

    def longestStrChain(self, words: List[str]) -> int:

        self.seen = {}

        def helper(word):
            if word in self.seen:
                return self.seen[word]

            if word not in words:
                return 0

            c = 1 + max([
                helper(word[:i] + word[i+1:])
                for i in range(len(word))
            ])
            self.seen[word] = c
            return c

        for word in words:
            helper(word)

        return max(self.seen.values())

