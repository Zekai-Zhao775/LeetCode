class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        # O(1)
        left = 0
        mid = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            mid_2 = mid * mid
            if mid_2 == x:
                return mid
            elif mid_2 > x and (mid - 1) * (mid - 1) < x:
                return mid - 1
            elif mid_2 > x:
                right = mid - 1
            elif mid_2 < x:
                left = mid + 1


class Solution:
    def mySqrt(self, x: int) -> int:
        # x 2^31, if we test one by one worst case it will be 2^16 = 16*16*16*16 = 65536
        # this size no need to do binary search
        i = 0
        while True:
            if i*i == x:
                return i
            elif i*i < x:
                i += 1
            elif i*i > x:
                return i - 1