from typing import List


def solution(nums: List[int]) -> List[int]:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    sum = 0
    result = []
    for num in nums:
        sum += num
        result.append(sum)
    return result


if __name__ == '__main__':
    print(solution(nums=[4, 5, 1, 6]) == [4, 9, 10, 16])
    print(solution(nums=[2, 2, 2, 2]) == [2, 4, 6, 8])
    print(solution(nums=[7, 3, 9, 4]) == [7, 10, 19, 23])
    print(solution(nums=[1, 2, 3]) == [1, 3, 6])