def solution(a: int, b: int) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    if a % b == 0:
        return a / b
    elif a == b:
        return 1
    else:
        return int(a / b + 1)

if __name__ == '__main__':
    print(solution(10, 1) == 10)
    print(solution(10, 2) == 5)
    print(solution(10, 3) == 4)