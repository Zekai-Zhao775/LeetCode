def solution(n: int) -> list:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    result = []
    i = n
    j = 0

    while i >= 0:
        j = 0
        while j < i:
            result.append(n - j)
            j += 1
        i -= 1
    return result

if __name__ == '__main__':
    print(solution(3) == [3, 2, 1, 3, 2, 3])
    print(solution(4) == [4, 3, 2, 1, 4, 3, 2, 4, 3, 4])
    print(solution(5) == [5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5])