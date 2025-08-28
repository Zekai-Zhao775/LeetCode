from typing import List


class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        # edge case
        if len(lights) == 1:
            return lights[0][0] - lights[0][1]
        start = []
        end = []
        for light in lights:
            start.append(light[0] - light[1])
            end.append(light[0] + light[1])
        start.sort()
        end.sort()

        brightness = 0
        brightness_max = 0
        brightness_max_position = 0

        i = 0
        j = 0
        while i < len(start):
            if j >= len(end):
                brightness += 1
                if brightness > brightness_max:
                    brightness_max = brightness
                    brightness_max_position = start[i]
            elif start[i] <= end[j]:
                brightness += 1
                while i < len(start) - 1 and start[i] == start[i + 1]:
                    brightness += 1
                    i += 1
                if brightness > brightness_max:
                    brightness_max = brightness
                    brightness_max_position = start[i]
                while j < len(end) and start[i] == end[j]:
                    j += 1
                    brightness -= 1
            elif start[i] > end[j]:
                while j < len(end) and start[i] > end[j]:
                    j += 1
                    brightness -= 1
                brightness += 1
                while i < len(start) - 1 and start[i] == start[i + 1]:
                    brightness += 1
                    i += 1
                if brightness > brightness_max:
                    brightness_max = brightness
                    brightness_max_position = start[i]
                while j < len(end) and start[i] == end[j]:
                    j += 1
                    brightness -= 1

            i += 1

        return brightness_max_position

# Wrong method, can be fixed, but it will be O(n*n)
# class Solution:
#     def brightestPosition(self, lights: List[List[int]]) -> int:
#         # edge case
#         if len(lights) == 1:
#             return lights[0][0] - lights[0][1]
#         covers = []
#         for light in lights:
#             covers.append([light[0] - light[1], light[0] + light[1]])
#         covers.sort(key=lambda x: (x[0], x[1]))
#         brightness_max = 0
#         brightness_max_position = 0
#         brightness = 0
#         cover_cur = []
#         last_start = 0
#         i = 0
#         while i < len(covers):
#             if cover_cur == []:
#                 brightness = 1
#                 cover_cur = covers[i]
#                 last_start = i
#             elif covers[i][0] > cover_cur[1]:
#                 if brightness > brightness_max:
#                     brightness_max = brightness
#                     brightness_max_position = cover_cur[0]
#                 brightness = 1
#                 i = last_start + 1
#                 last_start = i
#                 cover_cur = covers[i]
#             else:
#                 cover_cur = [max(cover_cur[0], covers[i][0]), min(cover_cur[1], covers[i][1])]
#                 brightness += 1
#             i += 1
#         if brightness > brightness_max:
#             brightness_max = brightness
#             brightness_max_position = cover_cur[0]
#         return brightness_max_position