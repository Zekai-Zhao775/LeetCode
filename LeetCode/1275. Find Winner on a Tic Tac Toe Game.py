class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        player = 'A'
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        for move in moves:
            if player == 'A':
                grid[move[0]][move[1]] = 'A'  # 'X'
                player = 'B'
            elif player == 'B':
                grid[move[0]][move[1]] = 'B'  # 'O'
                player = 'A'

        i = 0
        j = 0

        while i < 3:
            if grid[i][0] == grid[i][1] and grid[i][1] == grid[i][2]:
                return grid[i][0]
            i += 1

        while j < 3:
            if grid[0][j] == grid[1][j] and grid[1][j] == grid[2][j]:
                return grid[0][j]
            j += 1

        if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
            return grid[0][0]

        if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
            return grid[0][2]

        if len(moves) < 9:
            return "Pending"
        elif len(moves) == 9:
            return "Draw"