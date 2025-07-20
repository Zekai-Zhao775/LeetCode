class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word_start_index = -1
        word_end_index = -1
        i = 0
        while i < len(s):
            if s[i] == " ":
                if word_end_index != -1:
                    word_end_index = i
                    words.append(s[word_start_index:word_end_index])
                    word_start_index = -1
                    word_end_index = -1
            else:
                if word_start_index == -1:
                    word_start_index = i
                    word_end_index = i
                else:
                    word_end_index = i
            i += 1
        if word_end_index != -1:
            word_end_index += 1
            words.append(s[word_start_index:word_end_index])

        # print(words)

        if len(words) == 1:
            return "".join(words)

        words_reverse = []
        i = len(words) - 1
        while i >= 0:
            if i == len(words) - 1:
                words_reverse.append(words[i])
            else:
                words_reverse.append(" ")
                words_reverse.append(words[i])
            i -= 1
        return "".join(words_reverse)

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         words = []
#         temp = []
#         for char in s:
#             if char == ' ':
#                 if temp:
#                     words.append("".join(temp))
#                 temp = []
#             else:
#                 temp.append(char)

#         if temp:
#             words.append("".join(temp))

#         # print(words)

#         result = []
#         i = len(words) - 1
#         while i >= 0:
#             result.append(words[i])
#             result.append(" ")
#             i -= 1
#         result.pop()

#         return "".join(result)