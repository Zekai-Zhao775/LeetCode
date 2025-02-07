from typing import List


def solution(s: str, rules: List[int]) -> str:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    # O(n^2)
    i = 0
    j = 0
    target = 0
    result = []
    while j < len(rules):
        i = 0
        while i < len(rules):
            if rules[i] == target:
                result.append(s[i])
                # print("append" + s[i])
                target += 1
            i += 1
        j += 1
    return "".join(result)


if __name__ == '__main__':
    print(solution(s='hjklopmn', rules=[3, 6, 4, 1, 0, 2, 5, 7]) == 'olphkmjn')
    print(solution(s='xyz', rules=[2, 0, 1]) == 'yzx')
    print(solution(s='bad', rules=[1, 2, 0]) == 'dba')