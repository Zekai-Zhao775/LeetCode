from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # preprocessing
        # [0,1,1,1,0,1,1,0,1] ->
        # [0,3,0,2,0,1]
        numsNew = []
        countOne = 0
        for num in nums:
            if num == 1:
                countOne += 1
            else:
                if countOne != 0:
                    numsNew.append(countOne)
                    countOne = 0
                numsNew.append(0)
        if countOne != 0:
            numsNew.append(countOne)
            countOne = 0
        print(numsNew)

        if 0 not in numsNew:
            return sum(numsNew) - 1

        # initialize sliding window
        countZero = 0
        countOneMax = 0
        windowSize = 0
        for num in numsNew:
            if num != 0:
                countOneMax += num
                windowSize += 1
            else:
                if countZero == 1:
                    break
                countZero += 1
                windowSize += 1
        countOneTemp = countOneMax
        print(countOneMax)
        print(windowSize)

        i = 0
        while i < len(numsNew) - windowSize:
            # left == 0 and right == 0
            if numsNew[i] == 0 and numsNew[i + windowSize] == 0:
                i += 1
            # right != 0
            elif numsNew[i + windowSize] != 0:
                countOneTemp += numsNew[i + windowSize]
                windowSize += 1
                if countOneTemp > countOneMax:
                    countOneMax = countOneTemp
            # left != 0 and right == 0
            elif numsNew[i] != 0 and numsNew[i + windowSize] == 0:
                if countZero == 1:
                    countOneTemp -= numsNew[i]
                    windowSize -= 1
                    i += 1
                else:
                    countOneTemp += 1
                    windowSize += 1
                    countZero += 1
                    if countOneTemp > countOneMax:
                        countOneMax = countOneTemp

        return countOneMax