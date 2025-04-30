class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # sliding window O(n)
        countMax = 0
        for i in range(k):
            if self.isVowels(s[i]):
                countMax += 1
        countTemp = countMax
        for i in range(len(s) - k):
            if self.isVowels(s[i]):
                countTemp -= 1
            if self.isVowels(s[i + k]):
                countTemp += 1
            if countTemp > countMax:
                countMax = countTemp
            if countMax == k:
                return k
        return countMax

    def isVowels(self, s: str) -> bool:
        if s in ['a', 'e', 'i', 'o', 'u']:
            return True
        else:
            return False
