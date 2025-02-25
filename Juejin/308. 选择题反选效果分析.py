def solution(n: int, s: str, t: str) -> str:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    i = 0
    score = 0
    while i < n:
        if s[i] == t[i]:
            score += 1
        i += 1
    if score == (n /2):
        return "draw"
    elif score > (n / 2):
        return "no"
    else:
        return "yes"

if __name__ == '__main__':
    print(solution(2, "AB", "AA") == 'draw')
    print(solution(3, "BAA", "ABB") == 'yes')
    print(solution(4, "ABAB", "BABA") == 'yes')