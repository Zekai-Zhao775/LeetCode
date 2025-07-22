from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        move_flag = 0
        left_max = i
        right_max = j
        water_max = (j - i) * min(height[i], height[j])
        while i < j:
            water = (j - i) * min(height[i], height[j])
            if water >= water_max:
                left_max = i
                right_max = j
                if move_flag == 0:
                    move_flag = 1
                elif move_flag == 1:
                    move_flag = 0
            elif water < water_max:
                if move_flag == 0:
                    i += 1
                elif move_flag == 1:
                    j -= 1

        return water_max

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n**2)
        # iterate n*n to calculate every posibility
        # max = 0
        # temp = 0
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         temp = min(height[i], height[j]) * (j - i)
        #         if temp > max:
        #             max = temp
        # return max

        # O(n)
        # left and right pointer
        left = 0
        right = len(height) - 1
        max_area = min(height[left], height[right]) * (right - left)
        while left < right:
            # if we keep the shorter side, moving the longer side inside, it only decrease widths as well as area
            # so we move the shorter side
            if height[left] <= height[right]:
                left += 1
                max_area = max(max_area, (min(height[left], height[right]) * (right - left)))
            else:
                right -= 1
                max_area = max(max_area, (min(height[left], height[right]) * (right - left)))
        return max_area
