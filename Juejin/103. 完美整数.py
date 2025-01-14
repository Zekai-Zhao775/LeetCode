def solution(x, y):
    # Edit your code here
    i = x
    count = 0
    while i <= y:
        if perfectNum(i):
            count += 1
        i += 1
    return count


def perfectNum(x):
    if x >= 0 and x <= 9:
        return True
    else:
        x_new = x
        last_digits = x % 10
        while x_new >= 1:
            last_digits_new = x_new % 10
            if last_digits_new != last_digits:
                return False
            x_new = int(x_new / 10)

    return True


if __name__ == "__main__":
    # Add your test cases here

    print(solution(1, 10) == 9)
    print(solution(2, 22) == 10)