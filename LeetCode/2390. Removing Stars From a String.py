class Solution:
    def removeStars(self, s: str) -> str:
        i = 0
        sList = []

        for char in s:
            if char != '*':
                sList.append(char)
            else:
                sList.pop()

        return "".join(sList)
