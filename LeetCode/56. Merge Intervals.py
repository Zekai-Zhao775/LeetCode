from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interval_last = []
        start = 0
        end = 0
        result = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if len(result) == 0:
                result.append(interval)
            elif interval[0] > result[-1][1]:
                result.append(interval)
            else:
                # overlap
                result[-1][1] = max(interval[1], result[-1][1])
        return result