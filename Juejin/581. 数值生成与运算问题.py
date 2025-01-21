from typing import List


def solution(n: int, start: int) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    num = start + 2
    result = start
    while num <= start + 2 * n - 2:
        result ^= num
        num += 2
    return result


if __name__ == '__main__':
    print(solution(n=12, start=3) == 24)
    print(solution(n=20, start=16) == 0)
    print(solution(n=18, start=9) == 2)
    print(solution(n=7, start=1) == 15)