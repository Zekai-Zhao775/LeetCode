class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = []
        result = 0
        i = 0
        len_s = len(s)

        while i < len_s:
            nums.append(self.romanToInt_single(s[i]))
            i += 1

        i = 0
        while i < len_s - 1:
            if nums[i] >= nums[i + 1]:
                result += nums[i]
            else:
                result -= nums[i]
            i += 1
        result += nums[i]  # add last num

        return result

    def romanToInt_single(self, s):
        if s == 'I':
            return 1
        if s == 'V':
            return 5
        if s == 'X':
            return 10
        if s == 'L':
            return 50
        if s == 'C':
            return 100
        if s == 'D':
            return 500
        if s == 'M':
            return 1000

