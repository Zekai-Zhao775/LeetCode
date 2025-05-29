from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room: int):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)
        dfs(0)
        return len(rooms) == len(visited)