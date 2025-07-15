from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # O(n)
        real_cost = []
        for i in range(len(gas)):
            real_cost.append(gas[i] - cost[i])
        print(real_cost)
        if sum(real_cost) < 0:
            return -1
        # question -> start from i in real_cost, do sum (tank), tank always be positive
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += real_cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start

# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         # brute force, O(n*n) time
#         # if gas[i] < cost[i], skip
#         # if gas[i] == 0, skip
#         # start from a smart choice, when gas[i] - cost[i] == smallest, start at i + 1
#         gap = []
#         min_gap = gas[0] - cost[0]
#         min_gap_index = 0
#         for i in range(len(gas)):
#             gap.append(gas[i] - cost[i])
#             if gas[i] - cost[i] < min_gap:
#                 min_gap_index = i
#         tank = 0
#         if sum(gap) < 0:
#             return -1

#         k = (min_gap_index + 1) % len(gas)
#         for i in range(len(gas)):
#             if gas[(k + i) % len(gas)] >= cost[(k + i) % len(gas)] and gas[(k + i) % len(gas)] != 0:
#                 tank = 0
#                 for j in range(len(gas)):
#                     tank = tank + gas[(k + i + j) % len(gas)] - cost[(k + i + j) % len(gas)]
#                     if tank < 0:
#                         break
#                 if j == len(gas) - 1 and tank >= 0:
#                     return (k + i) % len(gas)
#         return -1