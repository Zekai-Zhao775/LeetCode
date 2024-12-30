def solution(s: str) -> str:
    # PLEASE DO NOT MODIFY THE FUNCTION SIGNATURE
    # write code here
    index_dot = s.find('.')
    index_last_0_at_front = -1
    len_s = len(s)

    if s[0] != '0':
        index_last_0_at_front = -1
    else:
        i = 0
        while i < len_s:
            if s[i] == '0':
                index_last_0_at_front += 1
                i += 1
            else:
                break

    if index_dot == -1:
        return solution_integer(s[index_last_0_at_front + 1:])
    else:
        return solution_integer(s[index_last_0_at_front + 1: index_dot]) + s[index_dot:]

def solution_integer(s: str) -> str:
    integer_part = []
    count_3 = 0
    len_s = len(s)
    i = len_s - 1
    while i >= 0:
        if count_3 == 3:
            integer_part.append(',')
            count_3 = 0
        else:
            integer_part.append(s[i])
            count_3 += 1
            i -= 1
    integer_part.reverse()
    return "".join(integer_part)

if __name__ == '__main__':
    print(solution("1294512.12412") == '1,294,512.12412')
    print(solution("0000123456789.99") == '123,456,789.99')
    print(solution("987654321") == '987,654,321')