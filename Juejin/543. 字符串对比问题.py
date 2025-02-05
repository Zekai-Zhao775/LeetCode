from typing import List


def solution(s: str) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    count = 0
    balance = 0
    for ch in s:
        if ch == 'L':
            balance += 1
        elif ch == 'R':
            balance -= 1
        if balance == 0:
            count += 1
    return count


if __name__ == '__main__':
    print(solution(s='LRLLRRLLRRLLRR') == 4)
    print(solution(s='RLRLRLRRRLLL') == 4)
    print(solution(s='RRLLLRLRRL') == 4)