from collections import defaultdict


class Solution:
    def romanToInt(self, s: str) -> int:
        # O(n) time, O(n) space
        result = []
        dict_roman = defaultdict(int)
        dict_roman["I"] = 1
        dict_roman["V"] = 5
        dict_roman["X"] = 10
        dict_roman["L"] = 50
        dict_roman["C"] = 100
        dict_roman["D"] = 500
        dict_roman["M"] = 1000
        dict_roman["IV"] = 4
        dict_roman["IX"] = 9
        dict_roman["XL"] = 40
        dict_roman["XC"] = 90
        dict_roman["CD"] = 400
        dict_roman["CM"] = 900
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                result.append(dict_roman[s[i]])
                i += 1
            else:
                if s[i:i+2] in dict_roman:
                    result.append(dict_roman[s[i:i+2]])
                    i += 2
                else:
                    result.append(dict_roman[s[i]])
                    i += 1
        return sum(result)


# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         nums = []
#         result = 0
#         i = 0
#         len_s = len(s)
#
#         while i < len_s:
#             nums.append(self.romanToInt_single(s[i]))
#             i += 1
#
#         i = 0
#         while i < len_s - 1:
#             if nums[i] >= nums[i + 1]:
#                 result += nums[i]
#             else:
#                 result -= nums[i]
#             i += 1
#         result += nums[i]  # add last num
#
#         return result
#
#     def romanToInt_single(self, s):
#         if s == 'I':
#             return 1
#         if s == 'V':
#             return 5
#         if s == 'X':
#             return 10
#         if s == 'L':
#             return 50
#         if s == 'C':
#             return 100
#         if s == 'D':
#             return 500
#         if s == 'M':
#             return 1000
#
