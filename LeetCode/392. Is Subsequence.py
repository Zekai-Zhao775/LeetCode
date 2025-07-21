class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if len(s) > len(t):
#             return False
#         index_s = 0
#         for i in range(len(t)):
#             if index_s < len(s):
#                 if t[i] == s[index_s]:
#                     index_s += 1
#             else:
#                 return True
#         if index_s == len(s):
#             return True
#         return False  