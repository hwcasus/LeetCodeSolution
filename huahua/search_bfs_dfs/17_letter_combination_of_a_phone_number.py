# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        self.ans = []
        def helper(digits, current):
            if len(digits) == 0:
                self.ans.append(current)
                return

            candidate = letters[int(digits[0])]
            for c in candidate:
                helper(digits[1:], current + c)

        if len(digits) > 0:
            helper(digits, "")

        return self.ans