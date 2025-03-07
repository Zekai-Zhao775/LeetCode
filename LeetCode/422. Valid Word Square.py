from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        words_list = []

        # turn to list
        for string in words:
            words_list.append(list(string))

        i = 0
        j = 0
        while i < len(words_list):
            j = 0

            while j < len(words_list[i]):
                if j >= len(words_list) or i >= len(words_list[j]):
                    return False
                if words_list[i][j] != words_list[j][i]:
                    return False
                j += 1

            i += 1

        return True



