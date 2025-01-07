def solution(n: int) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    team_left = n
    match_times = 0

    if n == 1:
        return 0

    while team_left >= 2:
        if team_left % 2 == 0:
            match_times += team_left / 2
            team_left /= 2
        else:
            match_times += (team_left - 1) / 2
            team_left = (team_left - 1) / 2 + 1

    return match_times


if __name__ == '__main__':
    print(solution(7) == 6)
    print(solution(14) == 13)
    print(solution(1) == 0)