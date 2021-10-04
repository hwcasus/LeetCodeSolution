# https://leetcode.com/problems/time-based-key-value-store/

import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._time = defaultdict(list)
        self._time_dict = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self._time_dict[(key, timestamp)] = value
        self._time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self._time[key], timestamp)
        if idx > 0:
            reduced_timestamp = self._time[key][idx - 1]
            value = self._time_dict.get((key, reduced_timestamp))
        else:
            value = ""
        return value

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)