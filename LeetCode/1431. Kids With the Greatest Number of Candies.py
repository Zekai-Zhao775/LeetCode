from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = -1
        for i in range(len(candies)):
            if candies[i] > max:
                max = candies[i]
            candies[i] += extraCandies

        result = []
        for i in range(len(candies)):
            if candies[i] >= max:
                result.append(True)
            else:
                result.append(False)

        return result