def solution(nums: list) -> bool:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    increase_flag = 0
    decrease_flag = 0
    i = 0
    if nums[1] - nums[0] >= 0:
        increase_flag = 1
        i = 2
        while i < len(nums):
            if nums[i] - nums[i - 1] < 0:
                increase_flag = 0
            i += 1
    elif nums[1] - nums[0] <= 0:
        decrease_flag = 1
        i = 2
        while i < len(nums):
            if nums[i] - nums[i - 1] > 0:
                decrease_flag = 0
            i += 1

    if increase_flag == 1 or decrease_flag == 1:
        return True
    return False


if __name__ == '__main__':
    print(solution(nums=[1, 2, 2, 3]) == True)
    print(solution(nums=[6, 5, 4, 4]) == True)
    print(solution(nums=[1, 3, 2, 4, 5]) == False)