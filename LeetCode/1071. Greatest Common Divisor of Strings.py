class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # find string for shorter str
        if len(str1) >= len(str2):
            str_short = str2
            str_long = str1
        else:
            str_short = str1
            str_long = str2

        str_short_divide = []
        i = len(str_short)
        while i >= 1:
            if len(str_short) % i == 0 and self.isDivided(str_short[:i], str_short):
                str_short_divide.append(str_short[:i])
            i -= 1

        for str in str_short_divide:
            if self.isDivided(str, str_long):
                return str

        return ""

    def isDivided(self, str1: str, str2: str) -> bool:
        # check if str1 divides str2 (AB, ABAB)
        if len(str2) % len(str1) != 0:
            return False
        if str2 == (str1 * int(len(str2) / len(str1))):
            return True
        else:
            return False

# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         str_result = ""

#         if len(str1) >= len(str2):
#             str_longer = str1
#             str_shorter = str2
#         else:
#             str_longer = str2
#             str_shorter = str1

#         # i = 1
#         # while i <= len(str_shorter):
#         #     str_temp = str_shorter[0:i]

#         #     if self.ifCanDivide(str_longer, str_temp) and self.ifCanDivide(str_shorter, str_temp):
#         #         str_result = str_temp

#         #     i += 1

#         # return str_result

#         i = len(str_shorter)
#         while i > 0:
#             str_temp = str_shorter[0:i]

#             if self.ifCanDivide(str_longer, str_temp) and self.ifCanDivide(str_shorter, str_temp):
#                 return str_temp

#             i -= 1

#         return str_result


#     def ifCanDivide(self, str1: str, str2: str) -> bool:
#         # if str1 can be divided by str2
#         if len(str1) % len(str2) != 0:
#             return False

#         i = 0
#         while i < len(str1):
#             if str2 == str1[i:i+len(str2)]:
#                 i += len(str2)
#                 continue
#             else:
#                 return False

#         return True