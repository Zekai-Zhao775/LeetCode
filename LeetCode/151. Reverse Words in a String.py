class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        temp = []
        for char in s:
            if char == ' ':
                if temp:
                    words.append("".join(temp))
                temp = []
            else:
                temp.append(char)

        if temp:
            words.append("".join(temp))

        # print(words)

        result = []
        i = len(words) - 1
        while i >= 0:
            result.append(words[i])
            result.append(" ")
            i -= 1
        result.pop()

        return "".join(result)