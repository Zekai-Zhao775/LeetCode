def solution(x: int, y: int) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    r = (x * x + y * y) ** 0.5
    if r > 11:
        return 0
    if r % 1 == 0:
        return 11-r
    else:
        return 11-int(r)-1


if __name__ == '__main__':
    print(solution(1, 0) == 10)
    print(solution(1, 1) == 9)
    print(solution(0, 5) == 6)
    print(solution(3, 4) == 6)