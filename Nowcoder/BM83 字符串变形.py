#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @param n int整型
# @return string字符串
#
class Solution:
    def trans(self, s: str, n: int) -> str:
        # write code here
        # scan, store every word, and do the filp at the same time
        words = []
        word = []
        for i in range(len(s)):
            if s[i] != ' ':
                if s[i] >= 'A' and s[i] <= 'Z':
                    word.append(s[i].lower())
                elif s[i] >= 'a' and s[i] <= 'z':
                    word.append(s[i].upper())
            else:
                words.append("".join(word))
                words.append(' ')
                word = []
        if len(word) != 0:
            words.append("".join(word))

        words.reverse()

        return "".join(words)