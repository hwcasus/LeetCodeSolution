# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0]]

        for layer in triangle[1:]:
            dp = [
                min(
                    dp[max(0, index - 1)],
                    dp[min(index, len(dp) - 1)]
                ) + element
                for index, element in enumerate(layer)
            ]

        return min(dp)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        for layer_idx in range(len(triangle) - 2, -1, -1):
            for element_idx in range(len(triangle[layer_idx])):
                triangle[layer_idx][element_idx] += min(
                    triangle[layer_idx + 1][element_idx: (element_idx + 1) + 1],
                )
        return triangle[0][0]