from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        numpad = []
        numpad.append([])
        numpad.append([])
        numpad.append(["a", "b", "c"])
        numpad.append(["d", "e", "f"])
        numpad.append(["g", "h", "i"])
        numpad.append(["j", "k", "l"])
        numpad.append(["m", "n", "o"])
        numpad.append(["p", "q", "r", "s"])
        numpad.append(["t", "u", "v"])
        numpad.append(["w", "x", "y", "z"])

        result = []
        path = []

        def phoneNumber(digits: str):
            if len(digits) == 1:
                for digit in numpad[int(digits[0])]:
                    path.append(digit)
                    result.append("".join(path))
                    path.pop()
                return
            else:
                for digit in numpad[int(digits[0])]:
                    path.append(digit)
                    phoneNumber(digits[1:])
                    path.pop()

        phoneNumber(digits)

        return result