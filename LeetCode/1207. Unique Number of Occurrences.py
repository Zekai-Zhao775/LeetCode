from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrDict = {}
        for num in arr:
            arrDict[num] = 0
        for num in arr:
            arrDict[num] += 1
        occurrences = set()
        for value in arrDict.values():
            occurrences.add(value)
        if len(arrDict) == len(occurrences):
            return True
        else:
            return False