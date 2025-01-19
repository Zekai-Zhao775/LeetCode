from typing import List


def solution(arr: List[int]) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    att_dict = {}
    for num in arr:
        if num in att_dict:
            att_dict[num] += 1
        else:
            att_dict[num] = 1

    key_max = -1
    for key in att_dict:
        if key == att_dict[key] and key > key_max:
            key_max = key

    return key_max


if __name__ == '__main__':
    print(solution(arr=[4, 3, 3, 2]) == -1)
    print(solution(arr=[1, 2, 2, 3, 3, 4, 4, 4, 4, 3]) == 4)
    print(solution(arr=[6, 6, 6, 6, 6]) == -1)