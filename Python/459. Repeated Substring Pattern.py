# BruteForce - list
# [0:n] use every substring to form the String
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """


        s_sub = ''
        s_new = []

        i = 1

        while i < len(s):
            s_new = []
            j = 0
            s_sub = s[0:i]
            if len(s) % len(s_sub) == 0:
                append_times = len(s) / len(s_sub)
                while j < append_times:
                    s_new.append(s_sub)
                    j += 1
                if "".join(s_new) == s:
                    return True

            i += 1
            s_new = []

        return False


# BruteForce - String
# [0:n] use every substring to form the String
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # BruteForce
        # [0:n] use every substring to form the String
        s_sub = ''
        s_new = ''

        i = 1

        while i < len(s):
            s_new = []
            j = 0
            s_sub = s[0:i]
            if len(s) % len(s_sub) == 0:
                append_times = int(len(s) / len(s_sub))
                s_new = s_sub * append_times
                if s_new == s:
                    return True

            i += 1
            s_new = []

        return False