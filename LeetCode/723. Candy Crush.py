from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        while True:
            # If three or more candies of the same type are adjacent vertically or horizontally,
            crush = []
            last_num = -1
            count_adj = 0
            for i in range(len(board)):
                count_adj = 0
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        count_adj = 0
                        last_num = -1
                    elif board[i][j] == last_num:
                        count_adj += 1
                        if count_adj == 3:
                            crush.append((i, j - 2))
                            crush.append((i, j - 1))
                            crush.append((i, j))
                        elif count_adj > 3:
                            crush.append((i, j))
                    else:
                        count_adj = 1
                        last_num = board[i][j]

            for j in range(len(board[0])):
                count_adj = 0
                for i in range(len(board)):
                    if board[i][j] == 0:
                        count_adj = 0
                        last_num = -1
                    elif board[i][j] == last_num:
                        count_adj += 1
                        if count_adj == 3:
                            crush.append((i - 2, j))
                            crush.append((i - 1, j))
                            crush.append((i, j))
                        elif count_adj > 3:
                            crush.append((i, j))
                    else:
                        count_adj = 1
                        last_num = board[i][j]
            if len(crush) == 0:
                break

            # crush them all at the same time - these positions become empty.
            for i, j in crush:
                board[i][j] = 0

            # After crushing all candies simultaneously, if an empty space on the board has candies on top of itself,
            # then these candies will drop until they hit a candy or bottom at the same time.
            # No new candies will drop outside the top boundary.
            for j in range(len(board[0])):
                column = []

                i = len(board) - 1
                while i >= 0:
                    if board[i][j] != 0:
                        column.append(board[i][j])
                    i -= 1

                i = len(board) - 1
                k = 0
                while i >= 0:
                    if k < len(column):
                        board[i][j] = column[k]
                        k += 1
                    else:
                        board[i][j] = 0
                    i -= 1
        return board