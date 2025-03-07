class Solution:
    def confusingNumber(self, n: int) -> bool:

        nums = []
        n_temp = n
        if n_temp == 0:
            nums.append(0)

        while n_temp >= 1:
            nums.append(n_temp % 10)
            n_temp = int(n_temp / 10)

        # valid?
        for num in nums:
            if num in [2, 3, 4, 5, 7]:
                return False

        # different?
        i = 0
        while i < len(nums):
            if nums[i] == 6:
                nums[i] = 9
            elif nums[i] == 9:
                nums[i] = 6
            i += 1

        if n == int("".join(map(str, nums))):
            return False
        else:
            return True


