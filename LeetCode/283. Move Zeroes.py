# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count_0 = 0
        nums_new = []

        for num in nums:
            if num == 0:
                count_0 += 1
            else:
                nums_new.append(num)

        i = 0
        while i < count_0:
            nums_new.append(0)
            i += 1

        # i = 0
        # while i < len(nums):
        #     nums[i] = nums_new[i]
        #     i += 1
        nums[:] = nums_new

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i_non_zero = 0
        i = 0

        while i < len(nums):
            if nums[i] != 0:
                nums[i_non_zero] = nums[i]
                i_non_zero += 1
            i += 1

        while i_non_zero < len(nums):
            nums[i_non_zero] = 0
            i_non_zero += 1
