class Solution:
    # int("101", 2) → interpret "101" as binary → decimal 5
    # int("77", 8) → interpret "77" as octal → decimal 63
    # int("1F", 16) → interpret "1F" as hexadecimal → decimal 31
    # int("123", 10) → interpret "123" as decimal → decimal 123
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]