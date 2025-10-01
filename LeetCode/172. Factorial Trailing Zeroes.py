class Solution:
    def trailingZeroes(self, n: int) -> int:
        # stupid to do it O(n)
        # do it O(1)
        # count how many X5 and X0 in it
        # so basically return // 5?
        # no, more like how many 5 in it, like for 25 it is two 5 there
        # 30: 5, 10, 15, 20, 25, 30
        # we can use n // 25 to count extrax 5
        # and n // 125
        # and so on
        return n // 5 + n // 25 + n // 125 + n // 625 + n // 3125