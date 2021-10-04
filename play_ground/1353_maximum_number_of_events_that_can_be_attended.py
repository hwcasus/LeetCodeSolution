# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        count = 0
        events = sorted(events, key=lambda x: x[1])
        max_date = events[-1][1]
        schedule = [False] * max_date

        for (start, end) in events:
            candidate_date = range(start-1, end)
            for date in candidate_date:
                if not schedule[date]:
                    schedule[date] = True
                    break

        return sum(schedule)
