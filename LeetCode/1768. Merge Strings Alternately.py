# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: str
#         """
#         output = []
#         i = 0
#         len1 = len(word1)
#         len2 = len(word2)
#
#         if len1 >= len2:
#             while i < len2:
#                 output.append(word1[i])
#                 output.append(word2[i])
#                 i += 1
#             output.append(word1[len2:])
#
#         if len2 >= len1:
#             while i < len1:
#                 output.append(word1[i])
#                 output.append(word2[i])
#                 i += 1
#             output.append(word2[len1:])
#
#         output = ''.join(output)
#         return output

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        len_min = min(len(word1), len(word2))

        i = 0
        while i < len_min:
            result.append(word1[i])
            result.append(word2[i])
            i += 1

        if len(word1) > len(word2):
            result.append(word1[i:])
        elif len(word1) < len(word2):
            result.append(word2[i:])

        return "".join(result)