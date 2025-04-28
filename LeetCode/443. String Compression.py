from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        result = []
        temp = ''
        count = 0
        count_append = ''
        i = 0
        for char in chars:
            if char != temp:
                if temp != '':
                    result.append(temp)
                    if count != 1:
                        count_append = str(count)
                        i = 0
                        while i < len(count_append):
                            result.append(count_append[i])
                            i += 1
                temp = char
                count = 1
            else:
                count += 1
        result.append(temp)
        if count != 1:
            count_append = str(count)
            i = 0
            while i < len(count_append):
                result.append(count_append[i])
                i += 1

        chars[:] = result
        return (len(chars))
