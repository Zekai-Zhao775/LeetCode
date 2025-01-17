def solution(S: str, T: str) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here

    # S_len - 公共前缀
    common_prefix_len = 0
    len_S = len(S)
    len_T = len(T)

    i = 0

    while i < min(len_S, len_T):
        if S[i] == T[i]:
            common_prefix_len += 1
        i += 1

    return len_S - common_prefix_len


if __name__ == '__main__':
    print(solution("aba", "abb") == 1)
    print(solution("abcd", "efg") == 4)
    print(solution("xyz", "xy") == 1)
    print(solution("hello", "helloworld") == 0)
    print(solution("same", "same") == 0)