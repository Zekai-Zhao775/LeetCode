class Solution:
    def hammingWeight(self, n: int) -> int:
        # Brian Kernighan’s Algorithm
        # remove mostright 0 everytime
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while n:
#             count += n & 1
#             # n >> 1, won't store!
#             n >>= 1
#         return count

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n).count("1")

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         n_b = bin(n)
#         for bit in n_b:
#             if bit == "1":
#                 count += 1
#         return count