from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # flowerbed.length == 1
        if len(flowerbed) == 1:
            if n == 0:
                return True
            elif n == 1 and flowerbed[0] == 0:
                return True
            else:
                return False

        # flowerbed.length >= 2
        # check fonrt and rear
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            flowerbed[len(flowerbed) - 1] = 1
            n -= 1

        i = 1
        while i <= len(flowerbed) - 2:
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                n -= 1
                i += 2
            else:
                i += 1

        if n <= 0:
            return True
        return False