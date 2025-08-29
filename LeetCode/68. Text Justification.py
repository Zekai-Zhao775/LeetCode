from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        temp = []
        temp_len = 0
        for word in words:
            if len(temp) == 0:
                temp.append(word)
                temp_len += len(word)
            elif len(word) + 1 + temp_len <= maxWidth:
                temp.append(word)
                temp_len += len(word) + 1
            else:
                result.append(temp)
                temp = []
                temp_len = 0
                temp.append(word)
                temp_len += len(word)
        if temp != []:
            result.append(temp)
        # print(result)

        for i in range(len(result) - 1):
            words = result[i]
            temp = []
            len_words = 0
            count_words = len(words)
            for word in words:
                len_words += len(word)
            len_total_space = maxWidth - len_words
            if count_words == 1:
                temp.append(words[0])
                temp.append(" " * len_total_space)
                result[i] = "".join(temp)
            elif len_total_space % (count_words - 1) == 0:
                len_space = len_total_space // (count_words - 1)
                for j in range(len(words)):
                    if j == 0:
                        temp.append(words[j])
                    else:
                        temp.append(" " * len_space)
                        temp.append(words[j])
                result[i] = "".join(temp)
            else:
                len_space = len_total_space // (count_words - 1)
                len_extra_space = len_total_space - len_space * (count_words - 1)
                for j in range(len(words)):
                    if j == 0:
                        temp.append(words[j])
                    else:
                        if len_extra_space != 0:
                            temp.append(" " * (len_space + 1))
                            len_extra_space -= 1
                        else:
                            temp.append(" " * (len_space))
                        temp.append(words[j])
                result[i] = "".join(temp)

        temp = []
        words = result[len(result) - 1]
        for j in range(len(words)):
            if j == 0:
                temp.append(words[j])
            else:
                temp.append(" ")
                temp.append(words[j])
        len_left_space = maxWidth - len("".join(temp))
        temp.append(" " * len_left_space)
        result[len(result) - 1] = "".join(temp)
        return result