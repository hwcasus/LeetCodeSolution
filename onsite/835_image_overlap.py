# https://leetcode.com/problems/image-overlap/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        return self.f(img1, img2)

    def f(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        size = len(img1)
        padded_size = 3 * size - 2
        overlap_size = 2 * size - 1

        padded_img2 = [[0 for _ in range(padded_size)] for _ in range(padded_size)]

        offset = size - 1
        for i in range(size):
            for j in range(size):
                padded_img2[i+offset][j+offset] = img2[i][j]

        result = 0

        for i_offset in range(overlap_size):
            for j_offset in range(overlap_size):
                s = sum([
                    padded_img2[i + i_offset][j + j_offset] * img1[i][j]
                    for i in range(size)
                    for j in range(size)
                ])
                result = max(result, s)

        return result
