class Solution:
    def reformatNumber(self, number: str) -> str:
        nums = []
        for c in number:
            if c != ' ' and c != '-':
                nums.append(c)

        i = 0
        result = []
        while len(nums) - i > 4:
            result.append("".join(nums[i:i + 3]))
            result.append('-')
            i += 3

        if len(nums) - i == 4:
            result.append("".join(nums[i:i + 2]))
            result.append('-')
            result.append("".join(nums[i + 2:i + 4]))
        elif len(nums) - i == 3:
            result.append("".join(nums[i:i + 3]))
        elif len(nums) - i == 2:
            result.append("".join(nums[i:i + 2]))

        return "".join(result)