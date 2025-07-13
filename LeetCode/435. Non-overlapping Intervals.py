from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time in descending order
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        count = 0

        i = 0
        while i < len(intervals) - 1:
            if intervals[i + 1][0] < intervals[i][1]:
                del intervals[i + 1]
                count += 1
            else:
                i += 1

        return count