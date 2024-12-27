class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # O(nlog(n)), using sort()
        # arr.sort()
        # arr_len = len(arr)
        # common_difference = arr[1] - arr[0]
        # i = 1
        # while i < len(arr):
        #     if (arr[i] - arr[i - 1]) !=  common_difference:
        #         return False
        #     i += 1
        # return True

        # O(n), (x-min)%d == 0
        max_arr = max(arr)
        min_arr = min(arr)
        len_arr = len(arr)
        if (max_arr - min_arr) % (len_arr - 1) != 0:
            return False
        common_difference = (max_arr - min_arr) / (len_arr - 1)
        # all the same
        if common_difference == 0:
            return True
        # need to check if there are same number
        if len(set(arr)) != len_arr:
            return False
        for num in arr:
            if (num - min_arr) % common_difference != 0:
                return False
        return True