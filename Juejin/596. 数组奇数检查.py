from typing import List


def solution(arr: List[int]) -> bool:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    count = 0
    for num in arr:
        if num % 2 == 1:
            count += 1
        else:
            count = 0
        if count >= 3:
            return True
    return False


if __name__ == '__main__':
    print(solution(arr=[4, 6, 3, 7, 9]) == True)
    print(solution(arr=[1, 2, 3, 4, 5]) == False)
    print(solution(arr=[10, 15, 17, 19, 20]) == True)
