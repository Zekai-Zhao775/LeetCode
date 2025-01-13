class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        len_s = len(s)
        len_t = len(t)

        i = 0

        while i < len_t:
            if t.count(t[i]) != s.count(t[i]):
                return t[i]
            i += 1