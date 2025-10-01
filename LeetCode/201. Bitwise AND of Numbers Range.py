# 14:28
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
         # can't be O(n) since n can be 2^31
         # how to make it log(n) then?
         # for num 0000 - 1000
         # first always be 0 since 0000, and last 3 will always be 0 since 1000

         # 5 0101 6 0100 7 0111
         # we first zfill the smaller number
         # then we take what is same in front and fill 0
        if left == right:
            return left
        left_b = bin(left)[2:].zfill(32)
        right_b = bin(right)[2:].zfill(32)
        result = ["0" for i in range(32)]
        for i in range(32):
            if left_b[i] == right_b[i]:
                result[i] = str(left_b[i])
            else:
                break
        return int("".join(result), 2)