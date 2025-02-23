def solution(n: int, x: int, a: list) -> str:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    total = 0
    for computer in a:
        total += computer

    return f"{total / 4 / x:.2f}"

if __name__ == '__main__':
    print(solution(4, 1, [2, 3, 4, 5]) == '3.50')
    print(solution(3, 2, [4, 6, 8]) == '2.25')
    print(solution(2, 1, [10, 5]) == '3.75')