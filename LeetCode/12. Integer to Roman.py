class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        while num != 0:
            if num >= 1000:
                result.append("M")
                num -= 1000
            elif num >= 900 and num < 1000:
                result.append("CM")
                num -= 900
            elif num >= 500 and num < 900:
                result.append("D")
                num -= 500
            elif num >= 400 and num < 500:
                result.append("CD")
                num -= 400
            elif num >= 100 and num < 400:
                result.append("C")
                num -= 100
            elif num >= 90 and num < 100:
                result.append("XC")
                num -= 90
            elif num >= 50 and num < 90:
                result.append("L")
                num -= 50
            elif num >= 40 and num < 50:
                result.append("XL")
                num -= 40
            elif num >= 10 and num < 40:
                result.append("X")
                num -= 10
            elif num >= 9 and num < 10:
                result.append("IX")
                num -= 9
            elif num >= 5 and num < 9:
                result.append("V")
                num -= 5
            elif num >= 4 and num < 5:
                result.append("IV")
                num -= 4
            elif num > 0 and num < 4:
                result.append("I")
                num -= 1
        return "".join(result)