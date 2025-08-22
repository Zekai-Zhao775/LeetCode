from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        if_newInterval_added = -1
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                result.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                if if_newInterval_added == -1:
                    if_newInterval_added = 1
                    result.append(newInterval)
                result.append(intervals[i])
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        if if_newInterval_added == -1:
            result.append(newInterval)

        return result