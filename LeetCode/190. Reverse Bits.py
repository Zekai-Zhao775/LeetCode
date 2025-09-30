class Solution:
    def reverseBits(self, n: int) -> int:
        # use [::-1] to reverse, [start:end:step]
        return int(bin(n)[2:].zfill(32)[::-1], 2)

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         n_b = bin(n)[2:].zfill(32)
#         n_b_reversed = []
#         i = len(n_b) - 1
#         while i >= 0:
#             n_b_reversed.append(n_b[i])
#             i -= 1
#         n_b_reversed = "".join(n_b_reversed)
#         return int(n_b_reversed, 2)