import heapq
from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # taskId -> (userId, priority)
        self.t = {}
        # heap stores (-priority, -taskId, userId)
        self.heap = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    # O(log(n))
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.t[taskId] = (userId, priority)
        # both descending
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    # O(log(n))
    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId not in self.t:
            return
        else:
            userId = self.t[taskId][0]
            self.t[taskId] = (userId, newPriority)
            # we will do lazy deletion later
            heapq.heappush(self.heap, (-newPriority, -taskId, userId))

    # O(1), lazy deletion later
    def rmv(self, taskId: int) -> None:
        if taskId not in self.t:
            return
        else:
            del self.t[taskId]

    def execTop(self) -> int:
        while self.heap:
            negP, negT, userId = self.heap[0]
            taskId = -negT
            # clean what has been romoved
            if taskId not in self.t:
                heapq.heappop(self.heap)
                continue
            # clean the one where priority changed
            if self.t[taskId][1] != -negP:
                heapq.heappop(self.heap)
                continue

            userId = self.t[taskId][0]
            heapq.heappop(self.heap)
            del self.t[taskId]
            return userId
        return -1

# class TaskManager:

#     def __init__(self, tasks: List[List[int]]):
#         # need to access task by id
#         self.t = defaultdict()
#         for task in tasks:
#             # key: taskId, value: [userId, priority]
#             self.t[task[1]] = [task[0], task[2]]

#     def add(self, userId: int, taskId: int, priority: int) -> None:
#         self.t[taskId] = [userId, priority]

#     def edit(self, taskId: int, newPriority: int) -> None:
#         self.t[taskId][1] = newPriority

#     def rmv(self, taskId: int) -> None:
#         # guarante task exists
#         del self.t[taskId]

#     # O(n)
#     def execTop(self) -> int:
#         task_id_highest_priority = -1
#         highest_priority = -1
#         user_id_highest_priority = -1
#         for task_id in self.t:
#             if self.t[task_id][1] > highest_priority:
#                 highest_priority = self.t[task_id][1]
#                 task_id_highest_priority = task_id
#             elif self.t[task_id][1] == highest_priority and task_id > task_id_highest_priority:
#                 task_id_highest_priority = task_id
#         if task_id_highest_priority == -1:
#             return -1
#         user_id_highest_priority = self.t[task_id_highest_priority][0]
#         self.rmv(task_id_highest_priority)
#         return user_id_highest_priority

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()