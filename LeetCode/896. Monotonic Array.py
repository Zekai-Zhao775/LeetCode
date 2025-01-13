class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        len_nums = len(nums)
        trend = nums[len_nums - 1] - nums[0]
        i = 0

        if trend > 0:
            i = 0
            while i < len_nums - 1:
                if nums[i + 1] - nums[i] < 0:
                    return False
                i += 1
        elif trend < 0:
            i = 0
            while i < len_nums - 1:
                if nums[i + 1] - nums[i] > 0:
                    return False
                i += 1
        else:
            i = 0
            while i < len_nums - 1:
                if nums[i + 1] - nums[i] != 0:
                    return False
                i += 1

        return True