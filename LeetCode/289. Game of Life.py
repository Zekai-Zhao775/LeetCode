from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        # board_copy = [[0 for _ in range(n)] for _ in range(m)]
        board_copy = [row[:] for row in board]
        # print(board_copy)

        # edge case
        if m == 1 and n == 1:
            board[0][0] = 0
            return
        elif m == 1 and n != 1:
            board[0][0] = 0
            board[0][n - 1] = 0
            if n == 2:
                return
            else:
                i = 1
                while i < n - 1:
                    if board_copy[0][i - 1] == 1 and board_copy[0][i + 1] == 1:
                        i += 1
                        continue
                    else:
                        board[0][i] = 0
                        i += 1
            return
        elif m != 1 and n == 1:
            board[0][0] = 0
            board[m - 1][0] = 0
            if m == 2:
                return
            else:
                i = 1
                while i < m - 1:
                    if board_copy[i - 1][0] == 1 and board_copy[i + 1][0] == 1:
                        i += 1
                        continue
                    else:
                        board[i][0] = 0
                        i += 1

            return
        # 010
        # 001
        # 111
        # 000
        i, j = 0, 0
        while i < m:
            j = 0
            while j < n:
                count = 0
                if i + 1 < m:
                    count += board_copy[i + 1][j]
                if i + 1 < m and j - 1 >= 0:
                    count += board_copy[i + 1][j - 1]
                if i + 1 < m and j + 1 < n:
                    count += board_copy[i + 1][j + 1]
                if j + 1 < n:
                    count += board_copy[i][j + 1]
                if j - 1 >= 0:
                    count += board_copy[i][j - 1]
                if i - 1 >= 0:
                    count += board_copy[i - 1][j]
                if i - 1 >= 0 and j - 1 >= 0:
                    count += board_copy[i - 1][j - 1]
                if i - 1 >= 0 and j + 1 < n:
                    count += board_copy[i - 1][j + 1]
                if count < 2:
                    board[i][j] = 0
                elif count == 2:
                    board[i][j] = board_copy[i][j]
                elif count == 3:
                    board[i][j] = 1
                elif count > 3:
                    board[i][j] = 0
                j += 1
            i += 1