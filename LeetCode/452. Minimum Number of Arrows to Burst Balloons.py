from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # romove the overlap balloons, return num left
        points.sort(key=lambda x: x[1])
        print(points)
        i = 0
        while i < len(points) - 1:
            if points[i][1] >= points[i + 1][0]:
                del points[i + 1]
            else:
                i += 1

        return len(points)