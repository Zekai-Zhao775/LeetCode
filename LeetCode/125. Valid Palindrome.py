class Solution:
    def isPalindrome(self, s: str) -> bool:
        # print(ord("A")) # 65
        # print(ord("Z")) # 90
        # print(ord("a")) # 97
        # print(ord("z")) # 122
        # print(ord("0")) # 48
        # print(ord("9")) # 57
        result = []
        for c in s:
            if ord(c) >= 97 and ord(c) <= 122:
                result.append(c)
            elif ord(c) >= 48 and ord(c) <= 57:
                result.append(c)
            elif ord(c) >= 65 and ord(c) <= 90:
                result.append(chr(ord(c) + 32))

        i = 0
        # print("".join(result))
        while i < len(result) // 2:
            if result[i] != result[-i - 1]:
                print(i)
                return False
            i += 1
        return True