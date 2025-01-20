from typing import List


def solution(n: int) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2

    num = [0, 1, 1]
    i = 0
    num_new = 0
    while i + 3 <= n:
        num_new = num[i] + num[i+1] + num[i+2]
        num.append(num_new)
        i += 1

    return num_new


if __name__ == '__main__':
    print(solution(n=5) == 7)
    print(solution(n=12) == 504)
    print(solution(n=18) == 19513)