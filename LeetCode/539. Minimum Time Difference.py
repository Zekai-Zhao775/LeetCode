from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # HH:MM -> MM(1440 max)
        for i in range(len(timePoints)):
            h = timePoints[i][:2]
            m = timePoints[i][3:5]
            timePoints[i] = int(h) * 60 + int(m)
        # print(timePoints)
        timePoints.sort()
        difference_min = 1440

        i = 0
        while i < len(timePoints) - 1:
            difference = min(timePoints[i + 1] - timePoints[i], 1440 - timePoints[i + 1] + timePoints[i])
            difference_min = min(difference_min, difference)
            i += 1

        difference = min(timePoints[i] - timePoints[0], 1440 - timePoints[i] + timePoints[0])
        difference_min = min(difference_min, difference)
        return difference_min