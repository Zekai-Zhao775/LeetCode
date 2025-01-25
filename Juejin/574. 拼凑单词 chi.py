from typing import List


def solution(text: str) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    count_c = 0
    count_h = 0
    count_i = 0
    for char in text:
        if char == 'c':
            count_c += 1
        if char == 'h':
            count_h += 1
        if char == 'i':
            count_i += 1
    return min(count_c, count_h, count_i)


if __name__ == '__main__':
    print(solution(text='chiichcc') == 2)
    print(solution(text='chicchcic') == 2)
    print(solution(text='cccchhii') == 2)