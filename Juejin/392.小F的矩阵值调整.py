def solution(a: list) -> list:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    for sublist in a:
        for i in range(len(sublist)):
            if sublist[i] % 2 == 0:
                sublist[i] *= 3
    return a

if __name__ == '__main__':
    print(solution([[1, 2, 3], [4, 5, 6]]) == [[1, 6, 3], [12, 5, 18]])
    print(solution([[7, 8, 9], [10, 11, 12]]) == [[7, 24, 9], [30, 11, 36]])
    print(solution([[2, 4], [6, 8]]) == [[6, 12], [18, 24]])