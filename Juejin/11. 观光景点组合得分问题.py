def solution(values: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    max_point = 0
    i = 0
    j = 0
    gap = 1
    len_values = len(values)
    while gap <= len_values - 1:
        i = 0
        j = i + gap
        while j < len_values:
            point = values[i] + values[j] + i - j
            if point > max_point:
                max_point = point
            i += 1
            j += 1
        gap += 1

    return max_point  # Placeholder return


if __name__ == '__main__':
    print(solution(values=[8, 3, 5, 5, 6]) == 11)
    print(solution(values=[10, 4, 8, 7]) == 16)
    print(solution(values=[1, 2, 3, 4, 5]) == 8)