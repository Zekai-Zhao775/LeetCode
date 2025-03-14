class Solution:
    def myPow(self, x: float, n: int) -> float:
        # O(n)
        # x multiply itself n times

        # O(log(n))
        nums = []
        result = 0.0
        x_new = x
        n_new = n

        if n == 0:
            return 1.00000

        elif n > 0:
            while n_new >= 2:
                if n_new % 2 == 0:
                    x_new *= x_new
                    n_new /= 2
                else:
                    nums.append(x_new)
                    x_new *= x_new
                    n_new = (n_new - 1) / 2
            result = x_new
            for num in nums:
                result *= num
            return result

        elif n < 0:
            while n_new <= -2:
                if n_new % 2 == 0:
                    x_new *= x_new
                    n_new /= 2
                else:
                    nums.append(x_new)
                    x_new *= x_new
                    n_new = (n_new + 1) / 2
            result = x_new
            for num in nums:
                result *= num
            result = 1 / result
            return result