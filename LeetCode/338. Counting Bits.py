from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0
        # 0, 0+1
        # 0, 1
        # 0, 1, 0+1, 1+1
        # 0, 1, 1, 2
        # 0, 1, 1, 2, 0+1, 1+1, 1+1, 2+1
        # ...
        if n == 0:
            return [0]
        repeat = [0]
        new = []
        i = 1
        while i <= n:
            if len(new) != len(repeat):
                new.append(repeat[i - len(repeat)] + 1)
                i += 1
            elif len(new) == len(repeat):
                repeat = repeat + new
                new = []

        return repeat + new