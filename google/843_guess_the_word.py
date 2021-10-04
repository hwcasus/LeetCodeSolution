# https://leetcode.com/problems/guess-the-word/

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

import numpy as np
class Solution:
    # https://leetcode.com/problems/guess-the-word/discuss/160945/Python-O(n)-with-maximum-overlap-heuristic
    # def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

    #     wordlist

    # def match(s1: str, s2: str) -> int
    #     return sum(c1 == c2 for c1, c2 in zip(s1, s2))

    def findSecretWordRaw(self, wordlist: List[str], master: 'Master') -> None:
        num_word = len(wordlist)

        diff = np.zeros((num_word, num_word))
        for i, word in enumerate(wordlist):
            for j, another_word in enumerate(wordlist):
                if j <= i:
                    continue
                difference = 6 - sum(
                    word[s] == another_word[s]
                    for s in range(6)
                )
                diff[i, j] = diff[j, i] = difference


        for _ in range(10):
            avg_diff = diff.mean(1)
            index = np.argmin(avg_diff)
            match_count = master.guess(wordlist[index])
            if match_count == 6:
                return

            diff_count = 6 - match_count
            # print("index", index)
            # print("diff_count", diff_count)
            # print("diff[index]", diff[index])

            excluded_idx, = np.where(diff[index] != diff_count)

            for idx in excluded_idx:
                diff[idx] = 6
                diff[:, idx] = 6
