from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        m = len(coordinates)

        i = 1
        if (coordinates[1][0] - coordinates[0][0]) == 0:
            while i < m:
                if coordinates[i][0] != coordinates[i - 1][0]:
                    return False
                i += 1
            return True


        i = 1
        b = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])

        while i < m:
            if (coordinates[i][0] - coordinates[i - 1][0]) == 0:
                return False
            else:
                b_temp = (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0])
                if b_temp != b:
                    return False
            i += 1
        return True
