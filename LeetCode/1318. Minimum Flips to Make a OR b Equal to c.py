class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            if bit_a == 0 and bit_b == 0 and bit_c == 1:
                count += 1
            elif bit_a == 1 and bit_b == 0 and bit_c == 0:
                count += 1
            elif bit_a == 0 and bit_b == 1 and bit_c == 0:
                count += 1
            elif bit_a == 1 and bit_b == 1 and bit_c == 0:
                count += 2
            a >>= 1
            b >>= 1
            c >>= 1
        return count

# class Solution:
#     def minFlips(self, a: int, b: int, c: int) -> int:
#         count = 0
#         bina = bin(a)[2:]
#         binb = bin(b)[2:]
#         binc = bin(c)[2:]
#         print(bina)
#         print(binb)
#         print(binc)
#         biggest_len = max(len(bina), len(binb), len(binc))
#         bina = "0" * (biggest_len - len(bina)) + bina
#         binb = "0" * (biggest_len - len(binb)) + binb
#         binc = "0" * (biggest_len - len(binc)) + binc
#         print(bina)
#         print(binb)
#         print(binc)
#         for i in range(biggest_len):
#             if bina[i] == "0" and binb[i] == "0" and binc[i] == "1":
#                 count += 1
#             elif bina[i] == "1" and binb[i] == "0" and binc[i] == "0":
#                 count += 1
#             elif bina[i] == "0" and binb[i] == "1" and binc[i] == "0":
#                 count += 1
#             elif bina[i] == "1" and binb[i] == "1" and binc[i] == "0":
#                 count += 2
#         return count