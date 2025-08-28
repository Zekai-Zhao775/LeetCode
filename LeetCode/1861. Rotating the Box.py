from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # drop stone then rotate
        for i in range(len(boxGrid)):
            j = len(boxGrid[0]) - 1
            bottom = len(boxGrid[0])
            while j >= 0:
                if boxGrid[i][j] == "*":
                    bottom = j
                elif boxGrid[i][j] == "#":
                    boxGrid[i][j] = "."
                    boxGrid[i][bottom - 1] = "#"
                    bottom -= 1
                j -= 1

        # rotate
        # 0,0 - 0,1
        box = [[] for i in range(len(boxGrid[0]))]
        for j in range(len(boxGrid[0])):
            for i in range(len(boxGrid)):
                box[j].append(boxGrid[len(boxGrid) - 1 - i][j])
        return box