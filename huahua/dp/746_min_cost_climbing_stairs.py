# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        accumulated_cost = [0] * len(cost)
        accumulated_cost[0] = cost[0]
        accumulated_cost[1] = cost[1]

        for i in range(2, len(cost)):
            accumulated_cost[i] = cost[i] + min(accumulated_cost[i-1], accumulated_cost[i-2])

        return min(accumulated_cost[-1], accumulated_cost[-2])