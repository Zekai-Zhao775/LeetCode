from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        # mark visited as "Y"
        def is_surrounded(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            if board[x][y] == "Y" or board[x][y] == "X":
                return True

            board[x][y] = "Y"
            up = is_surrounded(x - 1, y)
            down = is_surrounded(x + 1, y)
            left = is_surrounded(x, y - 1)
            right = is_surrounded(x, y + 1)

            return up and down and left and right

        # conver visited surrounded to "X"
        def convert(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if board[x][y] == "X":
                return
            else:
                board[x][y] = "X"
                convert(x - 1, y)
                convert(x + 1, y)
                convert(x, y - 1)
                convert(x, y + 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if is_surrounded(i, j):
                        convert(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "Y":
                    board[i][j] = "O"