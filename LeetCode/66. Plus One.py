class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        len_digits = len(digits)
        # last digit < 9
        if digits[len_digits - 1] < 9:
            digits[len_digits - 1] += 1
            return digits
        # 999...999
        all_nines = True
        for digit in digits:
            if digit != 9:
                all_nines = False
                break
        if all_nines == True:
            digits = [0] * (len_digits + 1)
            digits[0] = 1
            return digits
        #...9
        digits_int = 0
        for digit in digits:
            digits_int = digits_int*10 + digit
        digits_int += 1
        digits = list(map(int, str(digits_int)))
        return digits