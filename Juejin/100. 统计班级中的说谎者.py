def solution(A):
    # Edit your code here
    len_A = len(A)
    A.sort()  # 1 - 100

    if len_A % 2 == 0:
        liar = int(len_A / 2)
        last_score = A[int(len_A / 2)]
        i = int(len_A / 2) - 1
        while i >= 0:
            if A[i] == last_score:
                liar += 1
            i -= 1

        return liar

    if len_A % 2 != 0:
        liar = int(len_A / 2)
        last_score = A[int(len_A / 2)]
        i = int(len_A / 2)
        while i >= 0:
            if A[i] == last_score:
                liar += 1
            i -= 1
        return liar


if __name__ == "__main__":
    # Add your test cases here
    print(solution([100, 100, 100]) == 3)
    print(solution([2, 1, 3]) == 2)
    print(solution([30, 1, 30, 30]) == 3)
    print(solution([19, 27, 73, 55, 88]) == 3)
    print(solution([19, 27, 73, 55, 88, 88, 2, 17, 22]) == 5)