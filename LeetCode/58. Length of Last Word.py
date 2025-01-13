class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        i = len_s - 1
        flag_last_word = False
        len_last_word = 0

        while i >= 0:
            if s[i] == " ":
                if flag_last_word == True:
                    return len_last_word
                i -= 1
            else:
                len_last_word += 1
                flag_last_word = True
                i -= 1

        return len_last_word