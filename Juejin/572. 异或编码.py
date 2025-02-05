from typing import List


def solution(a: List[int], d0: int) -> List[int]:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    # A ^ B = result
    # A ^ result = B
    # b ^ result = A
    data = [d0]
    lastNum = d0
    for num in a:
        data.append(num ^ lastNum)
        lastNum = num ^ lastNum
    return data


if __name__ == '__main__':
    print(solution(a=[2, 5, 1], d0=3) == [3, 1, 4, 5])
    print(solution(a=[7, 4, 3], d0=6) == [6, 1, 5, 6])
    print(solution(a=[8, 1], d0=9) == [9, 1, 0])
    print(solution(a=[9, 2, 3], d0=4) == [4, 13, 15, 12])
    print(solution(a=[3, 6, 5], d0=7) == [7, 4, 2, 7])
