def solution(cards):
    # Edit your code here
    results = [0] * 1000

    for card in cards:
        results[card] += 1

    return results.index(1)


if __name__ == "__main__":
    # Add your test cases here

    print(solution([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 4)
    print(solution([0, 1, 0, 1, 2]) == 2)