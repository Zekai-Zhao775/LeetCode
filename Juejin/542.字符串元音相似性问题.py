from typing import List


def solution(s: str) -> bool:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    i = 0
    count_aeiou = 0

    while i < len(s) / 2:
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
            count_aeiou += 1
        i += 1

    while i < len(s):
        if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
            count_aeiou -= 1
        i += 1

    if count_aeiou == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(solution(s='applel') == True)
    print(solution(s='lemonjuice') == False)
    print(solution(s='abcdee') == False)