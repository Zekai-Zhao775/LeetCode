from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # find nearest heater for each house using binary search
        # return max distance
        houses.sort()
        heaters.sort()

        def nearest_heater_distance(house):
            # edge case
            if len(heaters) == 1:
                return abs(heaters[-1] - house)
            if house <= heaters[0]:
                return heaters[0] - house
            if house >= heaters[-1]:
                return house - heaters[-1]

            left = 0
            middle = 0
            right = len(heaters) - 1
            # find first heater >= house
            while left < right:
                middle = (left + right) // 2
                if house > heaters[middle]:
                    left = middle + 1
                else:
                    right = middle

            if abs(house - heaters[left]) < abs(house - heaters[left - 1]):
                return abs(house - heaters[left])
            else:
                return abs(house - heaters[left - 1])

        radius = 0
        for house in houses:
            distance = nearest_heater_distance(house)
            if distance > radius:
                radius = distance
        return radius

# class Solution:
#     def findRadius(self, houses: List[int], heaters: List[int]) -> int:
#         # simulation
#         # pick one house, caulculate min radius(binary search here?), pop all house being covered
#         # pick one from the left, repeat
#         # worst case
#         # O(n*logn*m)

#         # starting from radius 1
#         # reverse binary search here
#         # check houses in heaters O(nm)
#         # repeat times is log level and depends on constrains, so O(1)
#         # O(nm)
#         houses.sort()
#         heaters.sort()

#         # O(nm)
#         def all_cover(redius):
#             for house in houses:
#                 flag = False
#                 for heater in heaters:
#                     if house >= heater - redius and house <= heater + redius:
#                         flag = True
#                         break
#                 if not flag:
#                     return False
#             return True

#         # edge case
#         if all_cover(0):
#             return 0
#         if all_cover(1):
#             return 1

#         left = 0
#         right = 1
#         middle = 0
#         while not all_cover(right):
#             left = right
#             right *= 2

#         while left <= right:
#             middle = (left + right) // 2
#             if all_cover(middle):
#                 if not all_cover(middle - 1):
#                     return middle
#                 else:
#                     right = middle - 1
#             else:
#                 left = middle + 1