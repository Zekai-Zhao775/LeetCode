from typing import List


def solution(financials: List[List[int]]) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    money_max = 0
    i = 0

    for client in financials:
        money_temp = 0
        for money in client:
            money_temp += money
        if money_temp > money_max:
            money_max = money_temp


    return money_max


if __name__ == '__main__':
    print(solution(financials=[[2, 4, 6], [4, 3, 2]]) == 12)
    print(solution(financials=[[3, 9], [8, 2], [5, 6]]) == 12)
    print(solution(financials=[[5, 5, 9, 3], [6, 2, 3, 1], [3, 4, 10, 2]]) == 22)