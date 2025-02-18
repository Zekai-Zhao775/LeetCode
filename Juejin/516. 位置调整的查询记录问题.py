from typing import List


def solution(queries: List[int], m: int) -> List[int]:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    result = []
    per = []

    i = 1
    while i <= m:
        per.append(i)
        i += 1

    index = 0

    for q in queries:
        index = per.index(q)
        result.append(index)
        per.pop(index)
        per.insert(0, q)

    return result


if __name__ == '__main__':
    print(solution(queries=[2, 4, 1, 3], m=5) == [1, 3, 2, 3])
    print(solution(queries=[3, 2, 1, 4], m=4) == [2, 2, 2, 3])
    print(solution(queries=[1, 2, 1, 2], m=2) == [0, 1, 1, 1])
    print(solution(queries=[5, 4, 3, 2], m=6) == [4, 4, 4, 4])