def solution(a: int, b: int) -> str:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    return f"{(a * 9 + b * 9) / 4:.2f}"

if __name__ == '__main__':
    print(solution(3, 3) == '13.50')
    print(solution(5, 7) == '27.00')
    print(solution(1, 1) == '4.50')