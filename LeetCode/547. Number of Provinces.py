from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count_provinces = 0
        n = len(isConnected)

        def dfs(city: int) -> True:
            if city in visited:
                return False
            visited.add(city)
            i = 0
            while i < n:
                if isConnected[city][i] == 1:
                    dfs(i)
                i += 1
            return True

        i = 0
        while i < n:
            if dfs(i):
                count_provinces += 1
            i += 1
        return count_provinces
