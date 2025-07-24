from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        repet_check = [0] * 9
        print(repet_check)
        # check row
        for row in board:
            repet_check = [0] * 9
            for c in row:
                if c != ".":
                    repet_check[int(c) - 1] += 1
            for num in repet_check:
                if num > 1:
                    return False
        # check column
        i = 0
        j = 0
        while j < len(board[0]):
            repet_check = [0] * 9
            i = 0
            while i < len(board):
                if board[i][j] != ".":
                    repet_check[int(board[i][j]) - 1] += 1
                i += 1
            for num in repet_check:
                if num > 1:
                    return False
            j += 1

        # sub-boxes check
        i, ii, j, jj = 0, 0, 0, 0
        while i < len(board):
            j = 0
            while j < len(board[0]):
                repet_check = [0] * 9
                ii = i
                while ii < i + 3:
                    jj = j
                    while jj < j + 3:
                        if board[ii][jj] != ".":
                            # print("checking ii = ", ii, " jj = ", jj)
                            repet_check[int(board[ii][jj]) - 1] += 1
                        jj += 1
                    ii += 1
                for num in repet_check:
                    if num > 1:
                        return False
                j += 3
            i += 3
        return True