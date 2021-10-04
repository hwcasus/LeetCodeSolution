# https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row, column = len(dungeon), len(dungeon[0])
        for j in range(1, column):
            dungeon[0][j] += dungeon[0][j - 1]


        for i in range(1, row):
            dungeon[i][0] += dungeon[i-1][0]
            for j in range(1, column):
                dungeon[i][j] += max(dungeon[i-1][j], dungeon[i][j-1])

        return dungeon

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        hp = [[1001 for _ in range(n+1)] for _ in range(m+1)]
        hp[m][n-1] = hp[m-1][n] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                hp[i][j] = max(
                    1,
                    min(hp[i + 1][j], hp[i][j + 1]) - dungeon[i][j]
                )
        return hp[0][0]