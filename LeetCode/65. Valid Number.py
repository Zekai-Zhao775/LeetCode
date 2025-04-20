class Solution:
    def isNumber(self, s: str) -> bool:
        if len(s) == 0:
            return False
        if self.isInteger(s):
            return True
        elif self.isDecimal(s):
            return True
        else:
            # find 'e' or 'E'
            if 'e' in s:
                index = s.index("e")
            elif 'E' in s:
                index = s.index("E")
            else:
                return False

            if (self.isInteger(s[:index]) or self.isDecimal(s[:index])) and self.isExponent(s[index:]):
                return True
        return False

    def isDigits(self, s: str) -> bool:
        if len(s) == 0:
            return False
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for char in s:
            if char not in nums:
                return False
        return True

    def isInteger(self, s: str) -> bool:
        if len(s) == 0:
            return False
        # filter the valid "+" or "-"
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        return self.isDigits(s)

    def isDecimal(self, s: str) -> bool:
        if len(s) == 0:
            return False
        # filter the valid "+" or "-"
        if s[0] == '-' or s[0] == '+':
            s = s[1:]

        # find '.'
        if '.' not in s:
            return False
        index = s.index(".")

        # Digits followed by a dot
        if self.isDigits(s[:index]) and index == len(s) - 1:
            return True

        # Digits followed by a dot '.' followed by digits
        if self.isDigits(s[:index]) and self.isDigits(s[index + 1:]):
            return True

        # A dot '.' followed by digits.
        if s[0] == '.' and self.isDigits(s[index + 1:]):
            return True

        return False

    def isExponent(self, s: str) -> bool:
        if len(s) == 0:
            return False
        if s[0] == 'e' or s[0] == 'E':
            return self.isInteger(s[1:])
        return False
