def solution(points: list) -> bool:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
        return False

    if (points[0][0] - points[1][0]) / (points[0][1] - points[1][1]) == (points[1][0] - points[2][0]) / (
            points[1][1] - points[2][1]):
        return False

    return True


if __name__ == '__main__':
    print(solution(points=[[1, 1], [2, 3], [3, 2]]) == True)
    print(solution(points=[[1, 1], [2, 2], [3, 3]]) == False)
    print(solution(points=[[0, 0], [1, 1], [1, 0]]) == True)