class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x > 0 and x < 10:
            return True
        else:
            x_str = str(x)
            i = 0
            j = len(x_str) - 1
            while i <= j:
                if x_str[i] != x_str[j]:
                    return False
                i += 1
                j -= 1
            return True