from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        # edge case
        if len(queries) == 1:
            return [0]
        if n == 1:
            return [0] * len(queries)

        # O(n)
        result = []
        colors = [0] * n
        pairs_count = 0
        for q in queries:
            # before:
            before = 0
            i, color = q
            if i == 0:
                if colors[i] == colors[i + 1] and colors[i] != 0:
                    before += 1
            elif i == len(colors) - 1:
                if colors[i] == colors[i - 1] and colors[i] != 0:
                    before += 1
            else:
                if colors[i] == colors[i + 1] and colors[i] != 0:
                    before += 1
                if colors[i] == colors[i - 1] and colors[i] != 0:
                    before += 1
            # after
            after = 0
            colors[i] = color
            if i == 0:
                if colors[i] == colors[i + 1] and colors[i] != 0:
                    after += 1
            elif i == len(colors) - 1:
                if colors[i] == colors[i - 1] and colors[i] != 0:
                    after += 1
            else:
                if colors[i] == colors[i + 1] and colors[i] != 0:
                    after += 1
                if colors[i] == colors[i - 1] and colors[i] != 0:
                    after += 1
            pairs_count += after - before
            result.append(pairs_count)
        return result