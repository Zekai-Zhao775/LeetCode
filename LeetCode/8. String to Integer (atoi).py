class Solution:
    def myAtoi(self, s: str) -> int:
        result = []

        # filter the leading " "
        filtter_stop_flag = 0
        for char in s:
            if char == " " and filtter_stop_flag == 0:
                continue
            else:
                result.append(char)
                filtter_stop_flag = 1

        # "-" or "+"
        i = 0
        is_positive = 0
        if result == []:
            return 0

        if result[0] == "+":
            is_positive = 1
            i += 1
        elif result[0] == "-":
            is_positive = -1
            i += 1
        else:
            is_positive = 1

        #
        result_new = []
        while i < len(result):
            if result[i] >= "0" and result[i] <= "9":
                result_new.append(result[i])
            else:
                break
            i += 1

        if result_new == []:
            return 0
        else:
            result = int("".join(result_new)) * is_positive
            if result > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif result < 2 ** 31 * (-1):
                return 2 ** 31 * (-1)
            else:
                return result