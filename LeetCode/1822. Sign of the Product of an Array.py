class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute Force
        # product = 1
        # for num in nums:
        #     product *= num
        # if product > 0:
        #     return 1
        # elif product < 0:
        #     return -1
        # else:
        #     return 0

        # count
        count_negative = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                count_negative += 1
        if count_negative % 2 == 0:
            return 1
        else:
            return -1