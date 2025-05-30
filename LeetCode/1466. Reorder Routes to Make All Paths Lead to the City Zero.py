from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = dict()
        count = 0
        visited = {0}
        for a, b in connections:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b, 1))  # a -> b
            graph[b].append((a, 0))  # b -> a
            # {
            #     0: [(1, 1), (4, 0)],
            #     1: [(0, 0), (3, 1)],
            #     2: [(3, 1)],
            #     3: [(1, 0), (2, 0)],
            #     4: [(0, 1), (5, 1)],
            #     5: [(4, 0)]
            # }

        def dfs(city: int):
            nonlocal count
            for next_city in graph[city]:
                if next_city[0] not in visited:
                    visited.add(next_city[0])
                    if next_city[1] == 1:
                        count += 1
                    dfs(next_city[0])

        dfs(0)
        return count

    # def minReorder(self, n: int, connections: List[List[int]]) -> int:
    #     # time O(n^n)
    #     # space
    #     count = 0
    #     current = []
    #     next_city = [0]
    #     temp = 0
    #     i = 0
    #     pop_flag = -1
    #     while len(connections) != 0:
    #         current = next_city.copy()
    #         next_city = []
    #         i = 0
    #         while i < len(connections):
    #             pop_flag = 0
    #             for num in current:
    #                 if i < len(connections):
    #                     if num in connections[i] and connections[i][0] != num:
    #                         next_city.append(connections[i][0])
    #                         connections.pop(i)
    #                         pop_flag = 1
    #                     elif num in connections[i] and connections[i][0] == num:
    #                         next_city.append(connections[i][1])
    #                         connections.pop(i)
    #                         pop_flag = 1
    #                         count += 1
    #             if pop_flag == 0:
    #                 i += 1
    #     return count
