def solution(n: int) -> list:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    matrix = []
    for _ in range(n):
        matrix.append([0] * n)

    i = 0
    j = n - 1

    count = 1
    direction = 1  # 1 down 2 left 3 up 4 right

    border_down = n - 1
    border_left = 0
    border_up = 0
    border_right = n - 2

    while count <= n * n:
        matrix[i][j] = count
        count += 1

        # down
        if direction == 1:
            if i + 1 < border_down:
                i += 1
            else:
                i += 1
                border_down -= 1
                direction = 2  # turn left
        # left
        elif direction == 2:
            if j - 1 > border_left:
                j -= 1
            else:
                j -= 1
                border_left += 1
                direction = 3  # turn up
        # up
        elif direction == 3:
            if i - 1 > border_up:
                i -= 1
            else:
                i -= 1
                border_up += 1
                direction = 4  # turn right
        # right
        elif direction == 4:
            if j + 1 < border_right:
                j += 1
            else:
                j += 1
                border_right -= 1
                direction = 1  # turn down

    return matrix


if __name__ == '__main__':
    print(solution(4) == [[10, 11, 12, 1], [9, 16, 13, 2], [8, 15, 14, 3], [7, 6, 5, 4]])
    print(solution(5) == [[13, 14, 15, 16, 1], [12, 23, 24, 17, 2], [11, 22, 25, 18, 3], [10, 21, 20, 19, 4],
                          [9, 8, 7, 6, 5]])
    print(solution(3) == [[7, 8, 1], [6, 9, 2], [5, 4, 3]])