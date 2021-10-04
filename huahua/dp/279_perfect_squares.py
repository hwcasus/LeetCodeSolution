# https://leetcode.com/problems/perfect-squares/


class Solution:
    def numSquares(self, n: int) -> int:
        sq = [i**2 for i in range(1, int(n**0.5)+1)]
        visited = [False for _ in range(n+1)]
        queue = [n]
        step = 1

        while queue:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                for s in sq:
                    if curr > s:
                        if not visited[curr-s]:
                            queue.append(curr-s)
                            visited[curr-s] = True
                    elif curr == s:
                        return step

            step += 1

        return step

    def numSquares_dp(self, n: int) -> int:

        dp = [n for _ in range(n+1)]
        sq = [i**2 for i in range(1, int(n**0.5)+1)]

        if n in sq:
            return 1

        dp[0] = 0

        for i in range(1, n+1):
            cand = [dp[i - s] for s in sq if i >= s]
            dp[i] = min(cand) + 1

        return dp[-1]