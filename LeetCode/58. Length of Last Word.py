class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return 1
        start = 0
        end = -1
        i = len(s) - 1
        while i >= 0:
            if end == -1 and s[i] != " ":
                end = i
            elif end != -1 and s[i] == " ":
                start = i + 1
                break
            i -= 1
        return end - start + 1

# class Solution(object):
#     def lengthOfLastWord(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         len_s = len(s)
#         i = len_s - 1
#         flag_last_word = False
#         len_last_word = 0
#
#         while i >= 0:
#             if s[i] == " ":
#                 if flag_last_word == True:
#                     return len_last_word
#                 i -= 1
#             else:
#                 len_last_word += 1
#                 flag_last_word = True
#                 i -= 1
#
#         return len_last_word