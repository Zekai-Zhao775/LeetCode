def solution(a: int, b: int) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    if b == 0:
        return a * 10

    a_list = []
    i = a
    while i > 0:
        a_list.append(i % 10)
        i = (int)(i / 10)
    a_list.reverse()

    b_list = []
    i = b
    if b == 1:
        b_list.append(1)
    else:
        while i > 0:
            b_list.append(i % 10)
            i = (int)(i / 10)
        b_list.reverse()

    max_val = -1

    for pos in range(len(a_list) + 1):
        new_list = a_list[:pos] + b_list + a_list[pos:]

        candidate = 0
        for digit in new_list:
            candidate = candidate * 10 + digit

        if candidate > max_val:
            max_val = candidate

    return max_val


if __name__ == '__main__':
    print(solution(76543, 4) == 765443)
    print(solution(1, 0) == 10)
    print(solution(44, 5) == 544)
    print(solution(666, 6) == 6666)