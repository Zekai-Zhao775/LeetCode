from typing import List


def solution(instructions: List[str]) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    concentration = 0
    for s in instructions:
        if s == "++":
            concentration += 1
        else:
            concentration -= 1
    return concentration
    pass


if __name__ == '__main__':
    print(solution(instructions=['++', '--', '++']) == 1)
    print(solution(instructions=['++', '++', '--', '--']) == 0)
    print(solution(instructions=['++', '++', '--']) == 1)