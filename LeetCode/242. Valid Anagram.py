from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        for c in t:
            t_dict[c] += 1
        for c in s:
            if s_dict[c] != t_dict[c]:
                return False
        return True

# # O(n * 2)
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         len_s = len(s)
#         len_t = len(t)
#
#         if len_s != len_t:
#             return False
#
#         i = 0
#
#         while i < len_s:
#             if(s.count(s[i]) != t.count(s[i])):
#                 return False
#             else:
#                 i += 1
#
#         return True
#
# # O(n)
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         len_s = len(s)
#         len_t = len(t)
#
#         if len_s != len_t:
#             return False
#
#         frequency_s = {}
#         frequency_t = {}
#
#         i = 0
#
#         # while i < len_s:
#         #     frequency_s[s[i]] = frequency_s.get(s[i], 0) + 1
#         #     frequency_t[t[i]] = frequency_t.get(t[i], 0) + 1
#         #     i += 1
#
#         for char in s:
#             frequency_s[char] = frequency_s.get(char, 0) + 1
#         for char in t:
#             frequency_t[char] = frequency_t.get(char, 0) + 1
#
#         if frequency_s == frequency_t:
#             return True
#         else:
#             return False