class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for i in range(n)] for i in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        return self._check_winning()

    def _check_winning(self) -> int:
        # check horizontal
        for i in range(self.n):
            flag = self.board[i][0]
            for j in range(self.n):
                if self.board[i][j] != flag:
                    flag = 0
                    break
            if flag == 1 or flag == 2:
                return flag
        # check vertical
        for j in range(self.n):
            flag = self.board[0][j]
            for i in range(self.n):
                if self.board[i][j] != flag:
                    flag = 0
                    break
            if flag == 1 or flag == 2:
                return flag
        # check diagonal
        flag = self.board[0][0]
        for i in range(self.n):
            if self.board[i][i] != flag:
                flag = 0
                break
        if flag == 1 or flag == 2:
            return flag

        flag = self.board[0][self.n - 1]
        for i in range(self.n):
            if self.board[i][self.n - 1 - i] != flag:
                flag = 0
                break
        if flag == 1 or flag == 2:
            return flag
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)