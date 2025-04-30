from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # preprocessing
        # [1,1,1,0,0,0,1,1,1,1,0] ->
        # [3, 0, 0, 0, 4, 0] ->
        numsNew = []
        countOne = 0
        for num in nums:
            if num == 1:
                countOne += 1
            else:
                if countOne != 0:
                    numsNew.append(countOne)
                numsNew.append(0)
                countOne = 0
        if countOne != 0:
            numsNew.append(countOne)
        print(numsNew)

        # initialize countMax and sliding window
        countMax = 0
        countFlip = 0
        windowSize = 0
        for num in numsNew:
            if num != 0:
                countMax += num
                windowSize += 1
            else:
                if countFlip < k:
                    countMax += 1
                    countFlip += 1
                    windowSize += 1
                else:
                    break

        countTemp = countMax
        print(countMax)
        print(windowSize)

        i = 0
        while i < len(numsNew) - windowSize:
            # left == 0 and right == 0
            if numsNew[i] == 0 and numsNew[i + windowSize] == 0:
                i += 1
            # right != 0
            elif numsNew[i + windowSize] != 0:
                countTemp += numsNew[i + windowSize]
                windowSize += 1
                if countTemp > countMax:
                    countMax = countTemp
            # left != 0 and right == 0
            elif numsNew[i] != 0 and numsNew[i + windowSize] == 0:
                if countFlip == k:
                    countTemp -= numsNew[i]
                    i += 1
                    windowSize -= 1
                elif countFlip < k:
                    countTemp += 1
                    countFlip += 1
                    if countTemp > countMax:
                        countMax = countTemp

        return countMax