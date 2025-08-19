class Solution:
    def isHappy(self, n: int) -> bool:
        loop = set()
        while n != 0:
            loop.add(n)
            n_str = str(n)
            sum_squares = 0
            for c in n_str:
                sum_squares += int(c) * int(c)
            if sum_squares == 1:
                return True
            if sum_squares in loop:
                return False
            n = sum_squares
        return False