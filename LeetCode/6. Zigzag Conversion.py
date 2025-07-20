class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        words = [[] for i in range(numRows)]
        # print(words)
        for i in range(len(s)):
            state = i % (2 * numRows - 2)
            if state >= 0 and state <= numRows - 1:
                words[state].append(s[i])
            elif state >= numRows:
                words[2 * numRows - 2 - state].append(s[i])
            i += 1
        result = []
        for word in words:
            result.append("".join(word))
        return "".join(result)