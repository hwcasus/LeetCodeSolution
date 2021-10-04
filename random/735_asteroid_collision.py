# https://leetcode.com/problems/asteroid-collision/

# 本題其實重點在於思考一新的行星被加入時會怎麼處理
# 簡單來說就是會像是 stack 後進先出一樣, 從 stack 頂端拿出來比較
# 直到可以放進去為止.

class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        rest = []

        for i in range(len(a)):
            curr = a[i]
            while rest and curr < 0 < rest[-1]:
                prev = rest.pop()
                if prev == -curr:
                    curr = 0
                elif prev > -curr:
                    curr = prev

            if curr != 0:
                rest.append(curr)

        return rest