def solution(array):
    # Edit your code here
    for num in array:
        if array.count(num) > len(array) / 2:
            return num
    return False


if __name__ == "__main__":
    # Add your test cases here

    print(solution([1, 3, 8, 2, 3, 1, 3, 3, 3]) == 3)