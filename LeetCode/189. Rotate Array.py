from typing import List


class Solution:
    def gcd(self, a: int, b: int) -> int:
        """
        Euclidean Algorithm (辗转相除法)
        Return the greatest common divisor of a and b.
        """
        while b:
            a, b = b, a % b
        return a

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(n + k) time, O(k) space, create a list temp size of k
        # temp = []

        # O(n) time, O(1) space, move one num, store the replaced num, and then move the replaced num, total n times
        if k == 0:
            return
        count_move = 0
        temp = nums[0]
        temp_new = 0
        i = 0
        if self.gcd(len(nums), k) == 1:
            while count_move < len(nums):
                j = (i + k) % len(nums)
                temp_new = nums[j]
                nums[j] = temp
                temp = temp_new
                count_move += 1
                i = j
        else:
            total_iteration = self.gcd(len(nums), k)
            current_iteration = 0
            while current_iteration < total_iteration:
                count_move = 0
                temp = nums[current_iteration]
                temp_new = 0
                i = current_iteration
                while count_move < int(len(nums) / total_iteration):
                    j = (i + k) % len(nums)
                    temp_new = nums[j]
                    nums[j] = temp
                    temp = temp_new
                    count_move += 1
                    i = j
                current_iteration += 1