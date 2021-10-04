# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        max_area = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]] and stack[-1] != -1:
                height = heights[stack.pop()]
                width = (i - stack[-1]) - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
