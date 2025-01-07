def solution(n: int, nums: list) -> int:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    nums.sort()
    num_last = -0
    list_no_same_num = []

    for num in nums:
        if num != num_last:
            list_no_same_num.append(num)
            num_last = num

    if len(list_no_same_num) < 3:
        return list_no_same_num[-1]
    else:
        return list_no_same_num[-3]


if __name__ == '__main__':
    print(solution(3, [3, 2, 1]) == 1)
    print(solution(2, [1, 2]) == 2)
    print(solution(4, [2, 2, 3, 1]) == 1)