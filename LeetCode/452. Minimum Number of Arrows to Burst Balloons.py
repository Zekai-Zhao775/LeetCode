from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        # points.sort(key = lambda x: (x[0], x[1]))
        # print(points)
        last_end = - 2**32
        count = 0
        for i in range(len(points)):
            if points[i][0] <= last_end:
                count += 1
                last_end = min(last_end, points[i][1])
            else:
                last_end = points[i][1]
        return len(points) - count


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