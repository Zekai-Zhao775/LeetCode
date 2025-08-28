from typing import List


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # [3,1,0,0,0]:3 block have 0 black cell, 1 block have 1 balck cell
        coordinates_set = set()
        for coordinate in coordinates:
            coordinates_set.add((coordinate[0], coordinate[1]))

        block_accessed = set()
        result = [0, 0, 0, 0, 0]
        for node in coordinates:
            if node[0] - 1 >= 0 and node[1] - 1 >= 0:
                count = 0
                i = node[0] - 1
                j = node[1] - 1
                if (i, j) not in block_accessed:
                    if (i, j) in coordinates_set:
                        count += 1
                    if (i + 1, j) in coordinates_set:
                        count += 1
                    if (i, j + 1) in coordinates_set:
                        count += 1
                    if (i + 1, j + 1) in coordinates_set:
                        count += 1
                    result[count] += 1
                    block_accessed.add((i, j))
            if node[0] >= 0 and node[0] <= m - 2 and node[1] - 1 >= 0:
                count = 0
                i = node[0]
                j = node[1] - 1
                if (i, j) not in block_accessed:
                    if (i, j) in coordinates_set:
                        count += 1
                    if (i + 1, j) in coordinates_set:
                        count += 1
                    if (i, j + 1) in coordinates_set:
                        count += 1
                    if (i + 1, j + 1) in coordinates_set:
                        count += 1
                    result[count] += 1
                    block_accessed.add((i, j))
            if node[0] - 1 >= 0 and node[1] >= 0 and node[1] <= n - 2:
                count = 0
                i = node[0] - 1
                j = node[1]
                if (i, j) not in block_accessed:
                    if (i, j) in coordinates_set:
                        count += 1
                    if (i + 1, j) in coordinates_set:
                        count += 1
                    if (i, j + 1) in coordinates_set:
                        count += 1
                    if (i + 1, j + 1) in coordinates_set:
                        count += 1
                    result[count] += 1
                    block_accessed.add((i, j))
            if node[0] >= 0 and node[0] <= m - 2 and node[1] >= 0 and node[1] <= n - 2:
                count = 0
                i = node[0]
                j = node[1]
                if (i, j) not in block_accessed:
                    if (i, j) in coordinates_set:
                        count += 1
                    if (i + 1, j) in coordinates_set:
                        count += 1
                    if (i, j + 1) in coordinates_set:
                        count += 1
                    if (i + 1, j + 1) in coordinates_set:
                        count += 1
                    result[count] += 1
                    block_accessed.add((i, j))
        result[0] = (m - 1) * (n - 1) - sum(result[1:])
        return result

        # coordinates_set = set()
        # for coordinate in coordinates:
        #     coordinates_set.add((coordinate[0], coordinate[1]))

        # result = [0, 0, 0, 0, 0]
        # for i in range(m - 1):
        #     for j in range(n - 1):
        #         count = 0
        #         if (i, j) in coordinates_set:
        #             count += 1
        #         if (i + 1, j) in coordinates_set:
        #             count += 1
        #         if (i, j + 1) in coordinates_set:
        #             count += 1
        #         if (i + 1, j + 1) in coordinates_set:
        #             count += 1
        #         result[count] += 1
        # return result