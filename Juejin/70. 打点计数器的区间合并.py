def solution(inputArray):
    # Please write your code here
    result = set()
    for arr in inputArray:
        i = arr[0]
        while i <= arr[1]:
            result.add(i)
            i += 1

    return len(result)

if __name__ == "__main__":
    #  You can add more test cases here
    testArray1 = [[1,4], [7, 10], [3, 5]]
    testArray2 = [[1,2], [6, 10], [11, 15]]

    print(solution(testArray1) == 9 )
    print(solution(testArray2) == 12 )