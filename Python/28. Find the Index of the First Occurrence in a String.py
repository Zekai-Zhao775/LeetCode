# Cheat
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

# O(nm)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)

        len_haystack = len(haystack)
        len_needle = len(needle)

        i = 0
        j = 1
        flag = 0

        if len_needle > len_haystack:
            return -1

        while i < len_haystack:
            j = 0
            if haystack[i] == needle[0]:
                flag = 1
                while j < len_needle:
                    if i + j >= len_haystack:
                        return -1
                    if haystack[i + j] == needle[j]:
                        j += 1
                    else:
                        flag = 0
                        break
                if flag == 1:
                    return i
            i += 1

        return -1


# O(nm)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # return haystack.find(needle)

        len_haystack = len(haystack)
        len_needle = len(needle)

        i = 0

        if len_needle > len_haystack:
            return -1

        while i < len_haystack:
            if i + len_needle > len_haystack:
                return -1
            elif haystack[i:i + len_needle] == needle:
                return i
            else:
                i += 1

        return -1