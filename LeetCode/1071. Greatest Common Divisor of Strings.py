class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str_result = ""

        if len(str1) >= len(str2):
            str_longer = str1
            str_shorter = str2
        else:
            str_longer = str2
            str_shorter = str1

        # i = 1
        # while i <= len(str_shorter):
        #     str_temp = str_shorter[0:i]

        #     if self.ifCanDivide(str_longer, str_temp) and self.ifCanDivide(str_shorter, str_temp):
        #         str_result = str_temp

        #     i += 1

        # return str_result

        i = len(str_shorter)
        while i > 0:
            str_temp = str_shorter[0:i]

            if self.ifCanDivide(str_longer, str_temp) and self.ifCanDivide(str_shorter, str_temp):
                return str_temp

            i -= 1

        return str_result

    def ifCanDivide(self, str1: str, str2: str) -> bool:
        # if str1 can be divided by str2
        if len(str1) % len(str2) != 0:
            return False

        i = 0
        while i < len(str1):
            if str2 == str1[i:i + len(str2)]:
                i += len(str2)
                continue
            else:
                return False

        return True