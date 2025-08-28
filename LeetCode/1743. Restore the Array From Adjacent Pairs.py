from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # use adjacency list
        adj = defaultdict(list)
        for pair in adjacentPairs:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])

        # find the point has degree 1 (only connect to one point)
        start = 0
        for pair in adjacentPairs:
            if len(adj[pair[0]]) == 1:
                start = pair[0]
                break
            elif len(adj[pair[1]]) == 1:
                start = pair[1]
                break

        result = [start]
        last = start
        current = adj[start][0]
        result.append(current)
        while len(adj[current]) != 1:
            num1 = adj[current][0]
            num2 = adj[current][1]
            if num1 == last:
                last = current
                current = num2
                result.append(current)
            else:
                last = current
                current = num1
                result.append(current)

        return result