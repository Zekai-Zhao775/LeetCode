def solution(N: int, S: str) -> str:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    result = []
    for char in S:
        if char == "x":
            result.append("y")
        elif char == "y":
            result.append("x")
        elif char == "a":
            result.append("b")
        elif char == "b":
            result.append("a")
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    print(solution(N = 5, S = "xaytq") == 'ybxtq')
    print(solution(N = 6, S = "abcxyz") == 'bacyxz')
    print(solution(N = 3, S = "zzz") == 'zzz')