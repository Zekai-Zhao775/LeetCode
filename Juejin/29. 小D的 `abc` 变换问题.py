def solution(s: str, k: int) -> str:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    result = []
    i = 0
    string_temp = s

    while i < k:
        result.clear()
        for char in string_temp:
            if char == 'a':
                result.append('bc')
            elif char == 'b':
                result.append('ca')
            elif char == 'c':
                result.append('ab')
        string_temp = ''.join(result)
        i += 1

    return string_temp


if __name__ == '__main__':
    print(solution("abc", 2) == 'caababbcbcca')
    print(solution("abca", 3) == 'abbcbccabccacaabcaababbcabbcbcca')
    print(solution("cba", 1) == 'abcabc')