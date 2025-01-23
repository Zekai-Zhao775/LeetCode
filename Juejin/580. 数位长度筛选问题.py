from typing import List


def solution(nums: List[int]) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    count = 0
    for num in nums:
        if evenLength(num):
            count += 1
    return count

def evenLength(num: int) -> bool:
    num_temp = num
    count = 1
    while True:
        if num_temp / 10 >= 1:
            count += 1
            num_temp = (int)(num_temp / 10)
        else:
            break
    if count % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(solution(nums=[12, 345, 2, 6, 7896]) == 2)
    print(solution(nums=[555, 901, 482, 1771]) == 1)
    print(solution(nums=[1, 22, 333, 4444]) == 2)